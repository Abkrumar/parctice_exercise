from pathlib import Path
path = Path('/home/eric/data_files/text_files/Abubakar_Umar.txt')
content = path.read_text
print(content)
