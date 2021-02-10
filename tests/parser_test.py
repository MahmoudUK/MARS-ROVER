import unittest
from unittest import result

from marsrover.parser import (
    errorAndExit,
    parseAndExecute,
    parsePlateau,
    parseRoverCmds,
    parseRoverPosition,
    ParseException,
    parseRovers,
)


class ParserTests(unittest.TestCase):
    def test_errorAndExit_raises_SystemExit(self):
        # arrange
        message = "test"

        # act & assert
        with self.assertRaises(SystemExit) as cm:
            errorAndExit(message)

    def test_parseRoverPosition_for_valid_input_returns_rover_position(self):
        # arrange
        lineNumber = 1
        line = "1 2 N"

        # act
        result = parseRoverPosition(lineNumber, line)

        # assert
        self.assertEqual(
            result,
            (1, 2, "N"),
        )

    def test_parseRoverPosition_for_invalid_input_raises_parseException(self):
        # arrange
        lineNumber = 1
        line = "1 2 N V"

        # act & assert
        with self.assertRaises(ParseException):
            parseRoverPosition(lineNumber, line)

    def test_parseRoverCmds_for_valid_input_returns_RoverCmds(self):
        # arrange
        lineNumber = 1
        line = "LMLMLMLMM"

        # act
        result = parseRoverCmds(lineNumber, line)

        # assert
        self.assertEqual(
            result,
            "LMLMLMLMM",
        )

    def test_parseRoverCmds_for_invalid_input_raises_parseException(self):
        # arrange
        lineNumber = 1
        line = "LMLMLM XW O"

        # act & assert
        with self.assertRaises(ParseException):
            parseRoverCmds(lineNumber, line)

    def test_parsePlateau_for_invalid_input_format_raises_ParseException(self):
        # arrange
        file = iter(["5 5 4", "1 2 N", "LMLMLMLMM"])

        with self.assertRaises(ParseException):
            parsePlateau(file)

    def test_parsePlateau_for_invalid_input_values_raises_ParseException(self):
        # arrange
        file = iter(["5 x", "1 2 N", "LMLMLMLMM"])

        # act & assert
        with self.assertRaises(ParseException):
            parsePlateau(file)

    def test_parsePlateau_for_valid_input_returns_plateau_coordinates(self):
        # arrange
        file = iter(["1 2", "1 2 N", "LMLMLMLMM"])

        # act
        result = parsePlateau(file)

        # assert
        self.assertEqual(
            result,
            (1, 2),
        )

    def test_parseRovers_for_valid_input_returns_roverPosition_and_roverCmds(self):
        # arrange
        file = iter(["1 2 N", "LMLMLMLMM"])

        # act
        result = parseRovers(file)
        roverPosition, roverCmds = next(result)

        # assert
        with self.subTest():
            self.assertEqual(roverPosition, (1, 2, "N"))
        with self.subTest():
            self.assertEqual(roverCmds, "LMLMLMLMM")

    def test_parseAndExecute_for_invalid_or_missing_input_file_raises_SystemExit(self):
        # arrange
        fileName = ""

        # act & assert
        with self.assertRaises(SystemExit) as cm:
            parseAndExecute(fileName)

        self.assertEqual(cm.exception.code, 1)