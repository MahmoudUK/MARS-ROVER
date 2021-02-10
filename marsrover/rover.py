from .consts import NORTH, SOUTH, WEST, EAST, LEFT, RIGHT, MOVE


class Rover(object):
    """
    A class used to represent a Rover

    Attributes
    ----------
    xCoord : int
        represents the rover's x coordinates
    yCoord : int
        represents the rover's y coordinates
    orientation : str
        a letter representing one of the four cardinal compass points: 'N','E','S','W'

    Methods
    -------
    spinLeft()
        spins the rover 90 degrees left
    spinRight()
        spins the rover 90 degrees right
    move()
        moves the rover one grid point forward
    executeCommand()
        executes one of the following commands: spinLeft, spinRight or move
    executeCommands()
        executes a series of commands
    printPosition()
        prints out the rover's current position
    """

    def __init__(self, x: int = -1, y: int = -1, o: str = NORTH) -> object:
        """
        Parameters
        ----------
        x : int, optional
            the rover's x coordinates
        y : int, optional
            the rover's y coordinates
        o : str, optional
            the rover's orientation. a letter representing one of the four cardinal compass points: 'N','E','S','W'
        """
        self.xCoord = x
        self.yCoord = y
        self.orientation = o

    def isInRange(self, dimensions) -> bool:
        """Checks whether the rover's position is within the provided dimensions

        Parameters
        ----------
        dimensions : tuple
            the dimensions of the plateau, represented by a tuple of two integers (maxX, maxY)

        Returns
        -------
        bool
            True when the rover's position is within the provided dimensions, otherwise False
        """
        (maxX, maxY) = dimensions
        return 0 <= self.xCoord <= maxX and 0 <= self.yCoord <= maxY

    def spinLeft(self) -> None:
        """spins the rover 90 degrees left"""
        directionMap = {NORTH: WEST, WEST: SOUTH, SOUTH: EAST, EAST: NORTH}
        self.orientation = directionMap[self.orientation]

    def spinRight(self) -> None:
        """spins the rover 90 degrees right"""
        directionMap = {NORTH: EAST, WEST: NORTH, SOUTH: WEST, EAST: SOUTH}
        self.orientation = directionMap[self.orientation]

    def move(self) -> None:
        """moves the rover one grid point forward"""
        if self.orientation == NORTH:
            self.yCoord += 1
        elif self.orientation == EAST:
            self.xCoord += 1
        elif self.orientation == WEST:
            self.xCoord -= 1
        elif self.orientation == SOUTH:
            self.yCoord -= 1

    def executeCommand(self, command: str) -> None:
        """instruct the rover to execute one of the following methods: spinLeft, spinRight, or move

        Parameters
        ----------
        command : str
            one of the following letters 'L','R' and 'M'.
        """
        switch = {LEFT: Rover.spinLeft, RIGHT: Rover.spinRight, MOVE: Rover.move}
        switch[command](self)

    def executeCommands(self, cmds: str):
        """instruct the rover to execute a series of commands

        Parameters
        ----------
        cmds : str
            A string without empty spaces, constructed from the following letters 'L', 'R' and 'M'.
        """
        for cmd in cmds:
            self.executeCommand(cmd)

    def printPosition(self) -> None:
        """prints out the rover's current position in the following format: xCoord yCoord orientation"""
        print(f"{str(self.xCoord)} {str(self.yCoord)} {self.orientation}")
