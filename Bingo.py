import random


def roll_dice():

    return random.choice(range(1, 7)) + random.choice(range(1, 7))


def check_bingo(arr):

    if arr[0][0] and arr[0][1] and arr[0][2]:
        return True

    if arr[1][0] and arr[1][1] and arr[1][2]:
        return True

    if arr[2][0] and arr[2][1] and arr[2][2]:
        return True

    if arr[0][0] and arr[1][0] and arr[2][0]:
        return True

    if arr[0][1] and arr[1][1] and arr[2][1]:
        return True

    if arr[0][2] and arr[1][2] and arr[2][2]:
        return True

    if arr[0][0] and arr[1][1] and arr[2][2]:
        return True

    if arr[0][2] and arr[1][1] and arr[2][0]:
        return True

    return False


class Board(object):

    def __init__(self, nums):

        self.nums = nums
        self.reset()

    def reset(self):

        self.board = []
        for i in range(3):
            self.board.append([False, False, False])

    def mark_multiple(self, number):

        indices = []

        for i in range(3):
            for j in range(3):
                if (self.nums[i][j] % number == 0 and
                        self.board[i][j] is False):
                    indices.append((i, j))

        if len(indices) > 0:
            i, j = random.choice(indices)
            self.board[i][j] = True

    def check_bingo(self):
        return check_bingo(self.board)


n = 1000000
game = Board(
    [[12, 8, 20],
     [7, 18, 7],
     [20, 8, 12]]
)

num_trials = 0
total_trials = 0
num_wins = 0
three_wins = 0

for trial in range(n):

    num_trials += 1
    roll = roll_dice()
    game.mark_multiple(roll)
    if game.check_bingo():        
        total_trials += num_trials
        if num_trials == 3:
            three_wins += 1
        num_wins += 1
        num_trials = 0
        game.reset()

print('Average trials = {:3f}'.format(total_trials/num_wins))
print('#games won in three trials', three_wins)
