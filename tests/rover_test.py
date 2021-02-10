import unittest

from marsrover.rover import Rover


class RoverTests(unittest.TestCase):
    def test_isInRange_returns_false_when_rover_outside_dimensions(self):
        # arrange
        rover = Rover(1, 3, "N")

        # act
        result = rover.isInRange((1, 1))

        # assert
        self.assertEqual(
            result,
            False,
        )

    def test_isInRange_returns_true_when_rover_inside_dimensions(self):
        # arrange
        rover = Rover(1, 3, "N")

        # act
        result = rover.isInRange((4, 4))

        # assert
        self.assertEqual(
            result,
            True,
        )

    def test_spinLeft_for_north_oriented_rover(self):
        # arrange
        rover = Rover(0, 0, "N")

        # act
        rover.spinLeft()

        # assert
        self.assertEqual(
            rover.orientation,
            "W",
        )

    def test_spinRight_for_south_oriented_rover(self):
        # arrange
        rover = Rover(0, 0, "S")

        # act
        rover.spinRight()

        # assert
        self.assertEqual(
            rover.orientation,
            "W",
        )

    def test_move_for_north_oriented_rover(self):
        # arrange
        x = 0
        y = 0
        rover = Rover(x, y, "N")

        # act
        rover.move()

        # assert
        self.assertEqual(
            rover.yCoord,
            y + 1,
        )

    def test_move_for_east_oriented_rover(self):
        # arrange
        x = 0
        y = 0
        rover = Rover(x, y, "E")

        # act
        rover.move()

        # assert
        self.assertEqual(
            rover.xCoord,
            x + 1,
        )

    def test_move_for_south_oriented_rover(self):
        # arrange
        x = 2
        y = 2
        rover = Rover(x, y, "S")

        # act
        rover.move()

        # assert
        self.assertEqual(
            rover.yCoord,
            y - 1,
        )

    def test_executeCommand_for_L_executes_spinLeft(self):
        # arrange
        rover = Rover(0, 0, "N")

        # act
        rover.executeCommand("L")

        # assert
        self.assertEqual(
            rover.orientation,
            "W",
        )

    def test_executeCommand_for_R_executes_spinRight(self):
        # arrange
        rover = Rover(0, 0, "N")

        # act
        rover.executeCommand("R")

        # assert
        self.assertEqual(
            rover.orientation,
            "E",
        )

    def test_executeCommand_for_M_executes_move(self):
        # arrange
        x = 2
        y = 2
        rover = Rover(x, y, "N")

        # act
        rover.executeCommand("M")

        # assert
        self.assertEqual(
            rover.yCoord,
            y + 1,
        )

    def test_executeCommands_for_1_2_N_and_LMLMLMLMM(self):
        # arrange
        rover = Rover(1, 2, "N")

        # act
        rover.executeCommands("LMLMLMLMM")

        # assert
        with self.subTest():
            self.assertEqual(rover.xCoord, 1)
        with self.subTest():
            self.assertEqual(rover.yCoord, 3)
        with self.subTest():
            self.assertEqual(rover.orientation, "N")

    def test_executeCommands_for_3_3_E_and_MMRMMRMRRM(self):
        # arrange
        rover = Rover(3, 3, "E")

        # act
        rover.executeCommands("MMRMMRMRRM")

        # assert
        with self.subTest():
            self.assertEqual(rover.xCoord, 5)
        with self.subTest():
            self.assertEqual(rover.yCoord, 1)
        with self.subTest():
            self.assertEqual(rover.orientation, "E")