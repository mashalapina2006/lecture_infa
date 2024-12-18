notes_frequencies = {
    "C4": 261.63,
    "C#4/Db4": 277.18,
    "D4": 293.66,
    "D#4/Eb4": 311.13,
    "E4": 329.63,
    "F4": 349.23,
    "F#4/Gb4": 369.99,
    "G4": 392.00,
    "G#4/Ab4": 415.30,
    "A4": 440.00,
    "A#4/Bb4": 466.16,
    "B4": 493.88
}
frequency_input = float(input("Введите частоту звука (в Гц): ")
note_found = False
for note, frequency in notes_frequencies.items():
    if abs(frequency - frequency_input) <= 1: 
        print(f"Нота, соответствующая частоте {frequency_input} Гц: {note}")
        note_found = True
        break
if not note_found:
    print(f"Ноты, соответствующей введенной частоте {frequency_input} Гц, не существует.")
