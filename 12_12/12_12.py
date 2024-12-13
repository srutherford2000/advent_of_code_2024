from argparse import ArgumentParser

DIRECTIONS = [(0,1),(1,0),(0,-1),(-1,0)]

def get_rows(file_path):
    rows = []
    with open(file_path, "r") as open_file:
        for line in open_file:
            rows.append(line.strip())

    return rows

def find_continous_edge(edges, edge_dir, x,y, dx,dy):
    while(edge_dir, (x+dx,y+dy)) in edges:
        edges.remove((edge_dir, (x+dx,y+dy)))
        x += dx
        y += dy

def calc_straight_edges(edges):
    straight_edges = 0
    while len(edges)>0:
        straight_edges +=1
        edge_dir,(x,y) = edges.pop()
        
        #the edge is horizantal
        if edge_dir[0] == 0:
            find_continous_edge(edges, edge_dir, x,y,1,0)
            find_continous_edge(edges, edge_dir, x,y,-1,0)
        
        #the edge is vertical
        if edge_dir[1] == 0: 
            find_continous_edge(edges, edge_dir, x,y,0,1)
            find_continous_edge(edges, edge_dir, x,y,0,-1)

    return straight_edges
    

def recusive_search(x,y, let, rows, seen):
    if((x,y) in seen):
        return (0,[])
    else:
        total_arr = 1
        total_per = []
        seen.add((x,y))
        for dx, dy in DIRECTIONS:
            if(0<=x+dx<len(rows[0])) and (0<=y+dy<len(rows)) and (let == rows[y+dy][x+dx]):
                arr,per = recusive_search(x+dx, y+dy,let, rows, seen)
                total_arr+= arr
                total_per += per
            else:
                total_per.append(((dx,dy), (x, y)))
        return (total_arr, total_per)

def _12_12(rows):
    p1_total = 0
    p2_total = 0
    seen = set()
    for j in range(len(rows)):
        for i in range(len(rows[0])):
            arr,per = recusive_search(i,j,rows[j][i], rows, seen)
            p1_total += arr*len(per)
            p2_total += arr*calc_straight_edges(per)
    return p1_total, p2_total

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the input file")
    args = parser.parse_args()
    
    rows = get_rows(args.file_path)

    ans1, ans2 = _12_12(rows)
    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")