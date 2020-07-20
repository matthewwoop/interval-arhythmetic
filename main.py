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


def main():
    # Collect command line arguments
    args = build_argparser().parse_args()

    # load corresponding notes and intervals specified in args
    notes = load_notes(args.notes)
    print('Loaded notes: {}'.format(notes))

    intervals = load_intervals(args.intervals)
    print('Loaded intervals: {}'.format(intervals))


if __name__ == "__main__":
    main()