# Posture Tracker

A friend to help keep your posture consistent! 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Environment Setup

What things you need to install the software and how to install them. Follow 1. for conda and 2. for pip.

Using conda:
```
conda create --posture_tracker --requirements.txt
```

Using pip:
```
pip install -r requirements.txt
```

### Execution

Using the tool is simple! Once you've activated your environment, execute the following command.

The program will calibrate to how you're sitting in the first 2 seconds of execution. When you significantly deviate from that position, the program will give you a heads up. Oh no! I've moved and it thinks my posture is bad. Simply execute the below statement again to re-calibrate.

```
python posture_tracker/main.py
```

## Built With

* [opencv](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html) - Responsible for the computer vision

## Authors

Me!

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Shoutout to my momma. She rocks.
