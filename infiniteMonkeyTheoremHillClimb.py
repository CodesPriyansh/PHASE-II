import random 

goal_string = "i got murder on my mind by ynw melly" 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '] 

#generate the initial strings 
def generate_initial_strings():
    return ''.join(random.choice(letters) for _ in range(len(goal_string))) 

#write the scoring mechanism
def score(strings_for_score):
    return sum(1 for i in range(len(strings_for_score)) if strings_for_score[i] == goal_string[i]) 

#generate the neighbor strings which are different

def generate_neighbor(current_string):
    index = random.randint(0, len(goal_string) - 1)
    new_char = random.choice(letters)
    new_string = list(current_string)
    new_string[index] = new_char
    return ''.join(new_string)

#add all the functions

def main():
    current_string = generate_initial_strings()
    current_score = score(current_string) 
    
    best_string = current_string
    best_score = current_score
    
    iteration = 0
    
    while best_score < len(goal_string):
        neighbor = generate_neighbor(current_string)
        neighbor_score = score(neighbor)
        
        iteration += 1
        
        if neighbor_score > current_score:
            current_score = neighbor_score
            current_string = neighbor
            
            best_score = current_score
            best_string = current_string
            
            if iteration % 1000 == 0:
                print(f"iteration:{iteration}, best score:{best_score}, best string: {best_string}")
                
    print("final best score:", best_score)
    print("final best string:", best_string) 
    
if __name__ == '__main__':
    main() 
            
            
            
            