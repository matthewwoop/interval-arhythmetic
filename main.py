from argparse import ArgumentParser

from constants import NOTES, INTERVALS


def build_argparser():
    """
        Parse command line arguments

        :return: Instance of argument parser
    """

    parser = ArgumentParser()

    # NOTE: likely easier to move the above 2 into an -c, --config paramater
    # and adding a json/yaml file containing the user's desired settings
    parser.add_argument(
        '-n',
        '--notes',
        required=False,
        type=str,
        default='all',
        help=
        'A comma separated list of note names. Defaults to all notes in the octave.'
    )
    parser.add_argument(
        '--intervals',
        required=False,
        type=str,
        default='all',
        help=
        'A comma separated list of intervals in shorthand format (e.g. m2, P5, M7) Defaults to all intervals, not including extensions (9th).'
    )

    return parser


def load_notes(notes):
    """
        Uses command line arguments to load notes
    """

    if notes == 'all':
        notes = NOTES
    else:
        for note in notes:
            assert note in NOTES

    return notes


def load_intervals(intervals):
    """
        Uses command line arguments to load intervals

        Intervals are referenced by their shorthand
        e.g. M3, P4, 
    """

    if intervals == 'all':
        intervals = INTERVALS
    else:
        # NOTE: add try/except KeyError for non-supported intervals
        intervals = {INTERVALS[i] for i in intervals}

    return intervals


def generate_intervals(notes, intervals):
    """
        Creates a sentence describing the relationship between each note and the
        note located an interval's distance away in semitones.

        NOTE: Can definitely phrase that ^ better in the future lol
        NOTE: We're assuming ascending intervals for now, descening support
        would involve a factor of -1 in semitone distance
    """

    for k, v in intervals.items():
        interval_name = v['name']
        interval_dist = v['semitone_distance']

        print(interval_name.capitalize())
        print('=' * len(interval_name), '\n')

        for start_note in notes:
            end_note = compute_interval(start_note, interval_dist, scale=notes)
            print('A {} above {} is {}.'.format(interval_name, start_note,
                                                end_note))

        print('\n')


def compute_interval(start, semitones, scale=None):
    """
        Calculates the end note arrived at after travelling "n" semitones from
        the start note.

        start: string, e.g. 'A'
        semitones: int [0, 11]
        scale: list of notes ['A', ... , 'G#/Ab']
    """

    if scale is None:
        scale = load_notes('all')

    start_idx = scale.index(start)
    end_idx = (start_idx + semitones) % len(scale)

    return scale[end_idx]


def main():
    # Collect command line arguments
    args = build_argparser().parse_args()

    # load corresponding notes and intervals specified in args
    notes = load_notes(args.notes)
    print('\nLoaded notes: {}'.format(notes))

    intervals = load_intervals(args.intervals)
    print('\nLoaded intervals: {}'.format(intervals))

    print('\nGenerating Intervals\n')
    generate_intervals(notes, intervals)


if __name__ == "__main__":
    main()