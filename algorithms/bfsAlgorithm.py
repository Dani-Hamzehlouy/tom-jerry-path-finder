from collections import deque

from node import Node
from time import process_time


class AmplitudeAlgorithm:
    def __init__(self, world):
        self.emptyNode = Node(None, None, "first father", -1, 0, 0, 0)
        self.firstNode = Node(world, self.emptyNode, " ", 0, 0, 0, 0)
        self.tomPos = self.firstNode.searchForTom()
        self.stack = [self.firstNode]
        self.computingTime = ""
        self.length_world = world.shape[0]
        self.height_world = world.shape[1]

    def getComputingTime(self):
        return self.computingTime

    def setComputingTime(self, computingTime):
        self.computingTime = computingTime

    def start(self):
        startTime = process_time()

        queue = deque([self.firstNode])

        #stack = self.stack
        tomPos = self.tomPos
        currentNode = queue.popleft()
        expandedNodes = 0
        depth = 0

        #********************************************
        while  not (currentNode.isGoal()):

            expandedNodes += 1

            # Check if right side is free
            if not (tomPos[1] + 1 >= self.length_world) and currentNode.getState()[tomPos[0], tomPos[1] + 1] != 1:
                son = Node(currentNode.getState(), currentNode,
                                 "right", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                right = son.rightMovement(tomPos)
                son.setNewCost(right)
                son.setTomPos(right)
                son.moveRight(tomPos)
                if son.compareCicles2(right):
                    queue.append(son)
                    if son.getDepth() > depth:
                        depth = son.getDepth()

            # Check if left side is free
            if not (tomPos[1] - 1 < 0) and currentNode.getState()[tomPos[0], tomPos[1] - 1] != 1:
                son = Node(currentNode.getState(), currentNode,
                                "left", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                left = son.leftMovement(tomPos)
                son.setNewCost(left)
                son.setTomPos(left)
                son.moveLeft(tomPos)
                if son.compareCicles2(left):
                    queue.append(son)
                    if son.getDepth() > depth:
                        depth = son.getDepth()

            # Check if down side is free
            if not (tomPos[0] + 1 >= self.height_world) and currentNode.getState()[tomPos[0] + 1, tomPos[1]] != 1:
                son = Node(currentNode.getState(), currentNode,
                                "down", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                down = son.downMovement(tomPos)
                son.setNewCost(down)
                son.setTomPos(down)
                son.moveDown(tomPos)
                if son.compareCicles2(down):
                    queue.append(son)
                    if son.getDepth() > depth:
                        depth = son.getDepth()

            # Check if up side is free
            if not (tomPos[0] - 1 < 0) and currentNode.getState()[tomPos[0] - 1, tomPos[1]] != 1:
                son = Node(currentNode.getState(), currentNode,
                              "up", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                up = son.upMovement(tomPos)
                son.setNewCost(up)
                son.setTomPos(up)
                son.moveUp(tomPos)
                if son.compareCicles2(up):
                    queue.append(son)
                    if son.getDepth() > depth:
                        depth = son.getDepth()

            currentNode = queue.popleft()
            tomPos = currentNode.getTomPos()
        #********************************************\

        elapsedTime = (process_time() - startTime)
        elapsedTimeFormatted = "%.10f s." % elapsedTime
        self.setComputingTime(elapsedTimeFormatted)

        solution = currentNode.recreateSolutionWorld()
        solutionWorld = solution[::-1]
        print("Expanded nodes: ", expandedNodes)  # Good
        print("Depth: ", depth)
        print(" final cost of the solution is: " + str(currentNode.getCost()))
        print(currentNode.recreateSolution())
        return [solutionWorld, expandedNodes + 1, depth]