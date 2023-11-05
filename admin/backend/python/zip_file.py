from pathlib import Path
from zipfile import ZipFile

__OUTPUT_PATH = Path('../data/output/')
__FILE_PATH = Path('../data/output/')

def zip_file():
    save_file = __FILE_PATH / Path('tables.zip')
    zf = ZipFile(save_file,'w')
    file_path = __FILE_PATH
    for file in file_path.iterdir():
        if file.suffix != '.xlsx':
            continue
        path = Path(__OUTPUT_PATH) / Path(file.name)
        zf.write(path)
    zf.close()

# unit
# if __name__ == '__main__':
#     zip_file('test.zip')
