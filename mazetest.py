import maze
import pytest

@pytest.mark.parametrize('file, goalF',
                         [('maze1.txt',(0, 5)),
                          ('maze2.txt',(8, 13)),
                          ('maze3.txt',(2, 1)),
                          ('maze4.txt',(1, 10)),
                          ('maze5.txt',(0, 5))
                          ])


def test_prueba(file, goalF):
    m = maze.Maze(file)
    m.solve
    assert m.goal == goalF
