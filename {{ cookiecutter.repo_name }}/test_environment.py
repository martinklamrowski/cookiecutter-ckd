import sys

REQUIRED_PYTHON = "{{ cookiecutter.python_interpreter }}"


def main():
    system_major = sys.version_info.major
    if REQUIRED_PYTHON == "python3":
        required_major = 3
    else:
        raise ValueError("We're on Python 3 here. Unrecognized python interpreter: {}".format(REQUIRED_PYTHON))

    if system_major != required_major:
        raise TypeError(
            "This project requires Python 3. Found: Python {}".format(required_major, sys.version))
    else:
        print(">>> Development environment passes all tests!")


if __name__ == '__main__':
    main()
