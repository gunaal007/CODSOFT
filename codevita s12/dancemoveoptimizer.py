def minimum_moves(n, instructions):
    current_positions = set()
    for i in range(4):
        for j in range(i + 1, 4):
            current_positions.add((i, j))      
    tiles = {"up": 0, "down": 1, "left": 2, "right": 3}
        instruction_indices = [tiles[inst] for inst in instructions]
       for inst in instruction_indices:
        next_positions = set()
        for left, right in current_positions:
            if inst == left or inst == right:
               next_positions.add((left, right))
            else:
                next_positions.add((inst, right))
                next_positions.add((left, inst))
        current_positions = next_positions
        min_moves = float('inf')
    for left, right in current_positions:
        moves = sum(1 for inst in instruction_indices if inst != left and inst != right)