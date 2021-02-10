from .consts import *
from .rover import Rover
import sys


def errorAndExit(message):
    """Prints the provided message into the interpreter's stderr and exits with errors

    Parameters
    ----------
    message: str
        the error message
    """
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)


class ParseException(Exception):
    """A customized exception used when there are errors in parsing the input file

    Attributes
    ----------
    lineNumber : int
        the number of the line in the input file which has caused the exception
    message : str
        The message associated with this exception
    """

    def __init__(self, lineNumber, message):
        self.lineNumber = lineNumber
        self.message = message


def parseRoverPosition(lineNumber, line):
    """A function used to parse the rover's position from the input file

    Parameters
    ----------
    lineNumber : int
        the number of the parsed line in the input file
    line : str
        a string (line in the input file) that represents the rover's position

    Returns
    -------
    tuple
        a tuple of three values (xCoord:int, yCoord:int, orientation:str) representing the rover's position

    Raises
    ------
    ParseException
        when the input does not match the format which is expected for the rover's position
    """
    try:
        (xCoord, yCoord, orientation) = line.split()
    except ValueError:
        raise ParseException(lineNumber + 1, PARSE_ROVER_POSITION_ERROR_MESSAGE)
    if (
        not xCoord.isdigit()
        or not yCoord.isdigit()
        or not orientation in {NORTH, EAST, SOUTH, WEST}
    ):
        raise ParseException(lineNumber + 1, PARSE_ROVER_POSITION_ERROR_MESSAGE)
    return (int(xCoord), int(yCoord), orientation)


def parseRoverCmds(lineNumber, line):
    """A function used to parse the instructions sent to the rover from the input file

    Parameters
    ----------
    lineNumber : int
        the number of the parsed line in the input file
    line : str
        a line in the input file that represents a series of instructions sent to the rover

    Returns
    -------
    str
        a string that represents a series of commands for the rover to execute
    """
    line = line.strip()
    for char in line:
        if char not in {LEFT, RIGHT, MOVE}:
            raise ParseException(lineNumber + 1, PARSE_ROVER_CMD_ERROR_MESSAGE)
    return line


def parsePlateau(file):
    """A function used to parse the upper-right coordinates of the plateau from the input file

    Parameters
    ----------
    file : iterator
        iterator over the input file

    Returns
    -------
    tuple
        a tuple (maxX:int, maxY:int) represents the upper-right coordinates of the plateau

    Raises
    ------
    ParseException
        when the input does not match the format which is expected for the plateau coordinates
    """
    firstLine = next(file)
    try:
        (maxX, maxY) = firstLine.split()
    except ValueError:
        raise ParseException(1, PARSE_PLATEAU_SETUP_ERROR_MESSAGE)

    if not maxX.isdigit() or not maxY.isdigit():
        raise ParseException(1, PARSE_PLATEAU_SETUP_ERROR_MESSAGE)
    return (int(maxX), int(maxY))


def parseRovers(file):
    """A function used to parse the input lines for the rover's position and instructions

    Parameters
    ----------
    file : iterator
        iterator over the input file

    Returns
    -------
    tuple
        a tuple (roverPosition, roverCmds) represents the output of parsing the two consecutive lines
    """
    lines = enumerate(file)
    for (lineNumber, line) in lines:
        (nextLineNumber, nextLine) = next(lines)
        roverPosition = parseRoverPosition(lineNumber + 1, line)
        roverCmds = parseRoverCmds(nextLineNumber + 1, nextLine)
        yield (roverPosition, roverCmds)


def parseAndExecute(fileName: str) -> None:
    """A function used to parse and execute the instruction provided in the input file

    Parameters
    ----------
    fileName : str
        the name of the input text file

    Raises
    ------
    IOError
        when no input has been provided or there was an error reading the input file
    ParseException
        when the input does not match the expected format
    """
    try:
        with open(fileName, mode="r", encoding="utf-8-sig") as file:
            plateauSize = parsePlateau(file)
            for (roverPosition, roverCmds) in parseRovers(file):
                (x, y, o) = roverPosition
                r = Rover(x, y, o)
                r.executeCommands(roverCmds)
                if not r.isInRange(plateauSize):
                    errorAndExit(
                        f"Rover {r.xCoord} {r.yCoord} {r.orientation} is outside the plateau!"
                    )
                r.printPosition()
    except IOError as e:
        errorAndExit(f"Could not read file: {fileName}")
    except ParseException as e:
        errorAndExit(f"Invalid format on line {e.lineNumber}. {e.message}")
