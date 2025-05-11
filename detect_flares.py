#!/usr/bin/env python3
import argparse
from astropy.io import fits
import numpy as np
from astropy.time import Time

def load_lightcurve(lc_path):
    """Return times (unix s) and counts from a SoLEXS .lc FITS file."""
    with fits.open(lc_path) as hdul:
        data = hdul[1].data
    times = data['TIME']   # already unix seconds
    counts = data['COUNTS']
    return times, counts

def detect_spikes(times, counts, sigma=5):
    """Return sorted unique unix times where counts exceed median + sigma*std."""
    med, std = np.median(counts), np.std(counts)
    mask = counts > (med + sigma*std)
    return np.unique(times[mask])

def cluster_events(spike_times, gap=60):
    """
    Cluster unix timestamps into events: 
    gaps > `gap` seconds → new event.
    Returns list of (t_start, t_end) tuples.
    """
    if spike_times.size == 0:
        return []
    groups = [[spike_times[0]]]
    for t in spike_times[1:]:
        if t - groups[-1][-1] <= gap:
            groups[-1].append(t)
        else:
            groups.append([t])
    return [(g[0], g[-1]) for g in groups]

def format_event(event):
    """Convert a (t0, t1) unix pair to ISO and seconds-since-midnight."""
    t0, t1 = Time(event[0], format='unix'), Time(event[1], format='unix')
    # midnight of that day:
    mid = Time(t0.iso[:10]+'T00:00:00', format='isot', scale='utc')
    return {
        'start_iso': t0.iso,
        'end_iso':   t1.iso,
        'start_sod': (t0 - mid).sec,
        'end_sod':   (t1 - mid).sec
    }

def main():
    p = argparse.ArgumentParser(
        description="Detect and print flares from a SoLEXS .lc file"
    )
    p.add_argument('lc_file', help="Path to the .lc FITS file")
    p.add_argument('--sigma', type=float, default=5,
                   help="Threshold = median + sigma * std")
    p.add_argument('--gap',   type=int, default=60,
                   help="Seconds of inactivity to split events")
    args = p.parse_args()

    times, counts = load_lightcurve(args.lc_file)
    spikes = detect_spikes(times, counts, sigma=args.sigma)
    events = cluster_events(spikes, gap=args.gap)

    if not events:
        print("No flares detected.")
        return

    for i, ev in enumerate(events, 1):
        info = format_event(ev)
        print(f"Flare {i}: {info['start_iso']} → {info['end_iso']} "
              f"({info['start_sod']:.0f}s–{info['end_sod']:.0f}s since 00:00 UTC)")

if __name__ == '__main__':
    main()