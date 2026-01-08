import arcade
import random

# Game Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Tetris"
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20

# Colors
CYAN = arcade.color.CYAN
YELLOW = arcade.color.YELLOW
PURPLE = arcade.color.PURPLE
GREEN = arcade.color.GREEN
RED = arcade.color.RED
BLUE = arcade.color.BLUE
ORANGE = arcade.color.ORANGE
GRAY = arcade.color.GRAY
BLACK = arcade.color.BLACK
WHITE = arcade.color.WHITE

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]]   # J
]

COLORS = [CYAN, YELLOW, PURPLE, GREEN, RED, BLUE, ORANGE]


class Tetromino:
    def __init__(self):
        self.shape_index = random.randint(0, len(SHAPES) - 1)
        self.shape = [row[:] for row in SHAPES[self.shape_index]]
        self.color = COLORS[self.shape_index]
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = GRID_HEIGHT - 1

    def rotate(self):
        # Rotate the shape 90 degrees clockwise
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def get_width(self):
        return len(self.shape[0])

    def get_height(self):
        return len(self.shape)


class TetrisGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        # Game state
        self.grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = None
        self.next_piece = None
        self.game_over = False
        self.paused = False
        self.score = 0
        self.level = 1
        self.lines_cleared = 0

        # Timing
        self.fall_time = 0
        self.fall_speed = 0.5  # seconds

        # Offset for drawing
        self.grid_offset_x = 20
        self.grid_offset_y = 50

    def setup(self):
        """Set up the game"""
        self.grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.game_over = False
        self.paused = False
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.fall_time = 0
        self.fall_speed = 0.5
        self.spawn_piece()

    def spawn_piece(self):
        """Spawn a new piece"""
        if self.next_piece is None:
            self.current_piece = Tetromino()
            self.next_piece = Tetromino()
        else:
            self.current_piece = self.next_piece
            self.current_piece.x = GRID_WIDTH // 2 - self.current_piece.get_width() // 2
            self.current_piece.y = GRID_HEIGHT - 1
            self.next_piece = Tetromino()

        if self.check_collision(self.current_piece, 0, 0):
            self.game_over = True

    def check_collision(self, piece, offset_x, offset_y):
        """Check if piece collides with grid or boundaries"""
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = piece.x + x + offset_x
                    new_y = piece.y + y + offset_y

                    if new_x < 0 or new_x >= GRID_WIDTH or new_y < 0:
                        return True

                    if new_y < GRID_HEIGHT and self.grid[new_y][new_x] is not None:
                        return True
        return False

    def lock_piece(self):
        """Lock the current piece into the grid"""
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    grid_y = self.current_piece.y + y
                    grid_x = self.current_piece.x + x
                    if 0 <= grid_y < GRID_HEIGHT and 0 <= grid_x < GRID_WIDTH:
                        self.grid[grid_y][grid_x] = self.current_piece.color
        self.clear_lines()
        self.spawn_piece()

    def clear_lines(self):
        """Clear completed lines and update score"""
        lines_to_clear = []
        for y in range(GRID_HEIGHT):
            if all(self.grid[y][x] is not None for x in range(GRID_WIDTH)):
                lines_to_clear.append(y)

        for line in lines_to_clear:
            del self.grid[line]
            self.grid.append([None for _ in range(GRID_WIDTH)])

        if lines_to_clear:
            self.lines_cleared += len(lines_to_clear)
            # Scoring system
            if len(lines_to_clear) == 1:
                self.score += 100 * self.level
            elif len(lines_to_clear) == 2:
                self.score += 300 * self.level
            elif len(lines_to_clear) == 3:
                self.score += 500 * self.level
            elif len(lines_to_clear) == 4:
                self.score += 800 * self.level

            # Level up every 10 lines
            self.level = self.lines_cleared // 10 + 1
            self.fall_speed = max(0.1, 0.5 - (self.level - 1) * 0.05)

    def move(self, dx):
        """Move piece horizontally"""
        if not self.check_collision(self.current_piece, dx, 0):
            self.current_piece.x += dx

    def rotate_piece(self):
        """Rotate the current piece"""
        original_shape = [row[:] for row in self.current_piece.shape]
        self.current_piece.rotate()

        if self.check_collision(self.current_piece, 0, 0):
            # Try wall kicks
            for offset in [1, -1, 2, -2]:
                if not self.check_collision(self.current_piece, offset, 0):
                    self.current_piece.x += offset
                    return
            # If no valid position found, revert rotation
            self.current_piece.shape = original_shape

    def drop(self):
        """Drop piece one row"""
        if not self.check_collision(self.current_piece, 0, -1):
            self.current_piece.y -= 1
            return False
        else:
            self.lock_piece()
            self.fall_time = 0
            return True

    def hard_drop(self):
        """Drop piece to bottom instantly"""
        while not self.drop():
            self.score += 2

    def on_key_press(self, key, modifiers):
        """Handle key presses"""
        if self.game_over:
            if key == arcade.key.R:
                self.setup()
            elif key == arcade.key.Q:
                arcade.close_window()
        else:
            if key == arcade.key.LEFT:
                self.move(-1)
            elif key == arcade.key.RIGHT:
                self.move(1)
            elif key == arcade.key.DOWN:
                self.drop()
                self.fall_time = 0
            elif key == arcade.key.UP:
                self.rotate_piece()
            elif key == arcade.key.SPACE:
                self.hard_drop()
            elif key == arcade.key.P:
                self.paused = not self.paused

    def on_update(self, delta_time):
        """Update game state"""
        if self.game_over or self.paused:
            return

        self.fall_time += delta_time
        if self.fall_time >= self.fall_speed:
            self.drop()
            self.fall_time = 0

    def on_draw(self):
        """Draw everything"""
        arcade.start_render()

        # Draw grid
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                # Draw cell
                draw_x = self.grid_offset_x + x * BLOCK_SIZE
                draw_y = self.grid_offset_y + y * BLOCK_SIZE

                if self.grid[y][x] is not None:
                    arcade.draw_rectangle_filled(
                        draw_x + BLOCK_SIZE / 2,
                        draw_y + BLOCK_SIZE / 2,
                        BLOCK_SIZE - 2,
                        BLOCK_SIZE - 2,
                        self.grid[y][x]
                    )

                # Draw grid lines
                arcade.draw_rectangle_outline(
                    draw_x + BLOCK_SIZE / 2,
                    draw_y + BLOCK_SIZE / 2,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                    GRAY,
                    1
                )

        # Draw current piece
        if self.current_piece and not self.game_over:
            for y, row in enumerate(self.current_piece.shape):
                for x, cell in enumerate(row):
                    if cell:
                        draw_x = self.grid_offset_x + (self.current_piece.x + x) * BLOCK_SIZE
                        draw_y = self.grid_offset_y + (self.current_piece.y + y) * BLOCK_SIZE
                        arcade.draw_rectangle_filled(
                            draw_x + BLOCK_SIZE / 2,
                            draw_y + BLOCK_SIZE / 2,
                            BLOCK_SIZE - 2,
                            BLOCK_SIZE - 2,
                            self.current_piece.color
                        )

        # Draw next piece preview
        next_x = GRID_WIDTH * BLOCK_SIZE + self.grid_offset_x + 30
        next_y = SCREEN_HEIGHT - 100

        arcade.draw_text("NEXT:", next_x, next_y + 80, WHITE, 20, bold=True)

        if self.next_piece:
            for y, row in enumerate(self.next_piece.shape):
                for x, cell in enumerate(row):
                    if cell:
                        draw_x = next_x + x * 25
                        draw_y = next_y - y * 25
                        arcade.draw_rectangle_filled(
                            draw_x + 12,
                            draw_y + 12,
                            23,
                            23,
                            self.next_piece.color
                        )

        # Draw score and info
        info_x = next_x
        arcade.draw_text(f"SCORE:", info_x, next_y - 80, WHITE, 16, bold=True)
        arcade.draw_text(f"{self.score}", info_x, next_y - 110, WHITE, 20)

        arcade.draw_text(f"LEVEL:", info_x, next_y - 170, WHITE, 16, bold=True)
        arcade.draw_text(f"{self.level}", info_x, next_y - 200, WHITE, 20)

        arcade.draw_text(f"LINES:", info_x, next_y - 260, WHITE, 16, bold=True)
        arcade.draw_text(f"{self.lines_cleared}", info_x, next_y - 290, WHITE, 20)

        # Draw controls
        controls_y = 80
        arcade.draw_text("CONTROLS:", 20, controls_y - 30, WHITE, 12, bold=True)
        arcade.draw_text("←→: Move", 20, controls_y - 50, WHITE, 10)
        arcade.draw_text("↑: Rotate", 20, controls_y - 65, WHITE, 10)
        arcade.draw_text("↓: Soft Drop", 20, controls_y - 80, WHITE, 10)
        arcade.draw_text("SPACE: Hard Drop", 20, controls_y - 95, WHITE, 10)
        arcade.draw_text("P: Pause", 20, controls_y - 110, WHITE, 10)

        # Draw game over screen
        if self.game_over:
            arcade.draw_rectangle_filled(
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
                SCREEN_WIDTH - 40,
                200,
                (0, 0, 0, 230)
            )
            arcade.draw_text(
                "GAME OVER",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 + 40,
                RED,
                30,
                anchor_x="center",
                bold=True
            )
            arcade.draw_text(
                f"Final Score: {self.score}",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
                WHITE,
                20,
                anchor_x="center"
            )
            arcade.draw_text(
                "Press R to Restart",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 - 30,
                WHITE,
                16,
                anchor_x="center"
            )
            arcade.draw_text(
                "Press Q to Quit",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 - 55,
                WHITE,
                16,
                anchor_x="center"
            )

        # Draw pause screen
        if self.paused:
            arcade.draw_rectangle_filled(
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
                SCREEN_WIDTH - 40,
                100,
                (0, 0, 0, 200)
            )
            arcade.draw_text(
                "PAUSED",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2,
                WHITE,
                30,
                anchor_x="center",
                bold=True
            )


def main():
    """Main function"""
    game = TetrisGame()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
