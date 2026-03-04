import app.io.input as inp
import app.io.output as out

def main():
    inputs = [
        inp.read_from_console(),
        inp.read_file('D:/test.txt'),
        inp.read_file_with_pandas('D:/pandasTest.txt', ' ')
    ]
    for string in inputs:
        out.write_in_console(string)
        out.write_to_file(string, 'D:/output.txt', True)

if __name__ == '__main__':
    main()