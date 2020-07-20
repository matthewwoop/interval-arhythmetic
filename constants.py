NOTES = [
    'A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G',
    'G#/Ab'
]
"""
    Notes

    How do we want to handle the referencing of extensions and altered
    extensions
    e.g. flat 5, sharp 11, etc.
"""
INTERVALS = {
    'm2': {
        'name': 'minor 2nd',
        'semitone_distance': 1
    },
    'M2': {
        'name': 'major 2nd',
        'semitone_distance': 2
    },
    # ... Octave
}
