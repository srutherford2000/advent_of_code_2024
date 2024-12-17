from argparse import ArgumentParser
import heapq

RIGHT = {'E':'S', 'N':'E', 'W':'N', 'S':'W'}
LEFT = {'E':'N', 'N':'W', 'W':'S', 'S':'E'}
STRAIGHT = {'E':(1,0), 'N':(0,-1), 'W':(-1,0), 'S':(0,1)}
INT_MAX = 10**18

def get_rows(file_name):
    rows = []
    start = None
    end = None
    with open(file_name, "r") as open_file:
        for y,line in enumerate(open_file):
            line = line.strip()
            rows.append(line)
            for x,char in enumerate(line):
                if char == "E":
                    end = (x,y)
                elif char == "S":
                    start = (x,y)

    return start, end, rows

def min_score (scores, loc):
    the_min = INT_MAX
    for dir in RIGHT.values():
        the_min = min(the_min, scores[loc][dir])
    return the_min

def recurse_search(start_loc, start_dir):
    scores = {}
    for y in range(len(rows)):
        for x in range(len(rows[0])):
            scores[(x,y)] = {}
            for each_dir in RIGHT.values():
                scores[(x,y)][each_dir] = INT_MAX
    scores[(start_loc[0], start_loc[1], start_dir)] = 0

    priority_queue = [(0,start_loc, start_dir)]

    while len(priority_queue) > 0:
        new_score, (x,y), cur_dir = heapq.heappop(priority_queue)
        
        #move straight
        new_new_score = 1 + new_score
        new_x, new_y = x + STRAIGHT[cur_dir][0], y + STRAIGHT[cur_dir][1]
        if rows[new_y][new_x] != '#':
            if new_new_score < scores[(new_x, new_y)][cur_dir]:
                scores[(new_x, new_y)][cur_dir] = new_new_score
                heapq.heappush(priority_queue, (new_new_score, (new_x, new_y), cur_dir))

        new_new_score = new_score + 1000

        # Turn right
        new_dir_right = RIGHT[cur_dir]
        if new_new_score < scores[(x, y)][new_dir_right]:
            scores[(x, y)][new_dir_right]= new_new_score
            heapq.heappush(priority_queue, (new_new_score, (x, y), new_dir_right))

        # Turn left
        new_dir_left = LEFT[cur_dir]
        if new_new_score < scores[(x, y)][new_dir_left]:
            scores[(x, y)][new_dir_left] = new_new_score
            heapq.heappush(priority_queue, (new_new_score, (x, y), new_dir_left))
    
    return scores



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    start, end, rows = get_rows(args.file_path)

    scores = recurse_search(start, 'E')

    """    
    for y in range(len(rows)):
        row = ""
        for x in range(len(rows[0])):
            if rows[y][x] == "#":
                row += "[#####]"
            else:
                row+=f"[{str(min_score(scores, (x,y)))[:5].zfill(5)}]"
        print(row)
    """


    print(f"Part 1: {min_score(scores, end)}")



