l = []         # 이것이다. 이것이 바로 텍스트 파일을 array 로 옮긴 것이다. 
with open('C:/Users/path/filename.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if len(line) > 0:
            l.append(list(map(int, line.split(','))))

# 1000 by 1000 상황 가정 
import random
a = 0 
b= []
while a < 10 : 
    tour = random.sample(range(1000),1000) # 1000 by 1000 이기 때문에 1000 / 아니면 바꿔서 해도 됨
    A=tour.index(0)
    tour.pop(A)
    tour = [0] + tour + [0]
    b.append(tour)
    a = a+1 
    if a== 10:      # 한마디로 tour 를 10번 만든 것 
        break
        
c = 0 
d= []
while c <10: 
    
    bb = b[c]        # b는 경로다 c 는 그 경로의 각 행을 따낸 것
    e = 0 
    f =[]      # 이제부터는 각 경로를 따냈으니까 도시별 이동 거리 합을 구할거임
    
    while e<1000: 
        x,y =bb[e], bb[e+1]
        ee = l[x][y]        # bb 즉, 각 경로의 1,2번째 도시 간의 좌표를 구하고
        f.append(ee)        # 그 거리를 l 행렬에서 찾아서 한 줄로 만든후에
        e = e+1             # 다 더할 계획
        if e == 1000 :
            break
            
    sum1 = sum(f)     # 각 경로들마다 걸리는 거리의 총합을 구한것 
    d.append(sum1)      
    c=c+1
    
    if c ==10 :
        break
d_min = min(d)        # 거리들 중에서 가장 작은 값 캐치해내는 것 
AA=d.index(d_min)     # 그 최솟값을 찾아내는 과정 
parent = b[AA]        # 그 최솟값을 기록한 경로를 부모로 선정  # 부모로 선정되었으면 위의 과정과 똑같이 경로 재 설정
        
Bignumber = 0
while Bignumber < 35000 :
    
    parent = parent[1:1000]
    g = 0 
    child_list=[]    # child 리스트를 만드는 과정 시작 
    while g < 20:
        [i,j] = sorted(random.sample(range(1000),2))
        child =  parent[:i] + parent[j:j+1] +  parent[i+1:j] + parent[i:i+1] + parent[j+1:];
        child = [0] + child + [0]    # child 리스트를 다시 만듬 
        # parent list 를 무작위로 섞어서 child 리스트 생성 
        child_list.append(child) # child 리스트 한데 모아서  # 근데 이게 또 다른 리스트가 되어 버림
        g = g+1 
        if g == 20 : 
            break
            # child_list 생성까지는 성공 이 후에 오류 주의 
        
    parent = [0]+parent+[0]
    New_set =[]      # 새로운 set 를 만들어서 
    New_set.append(parent)
    AAAAA = 0 
    while AAAAA < 20:
        child_element = child_list[AAAAA]    # 부모와 
         
        New_set.append(child_element)           # 자식 세대들을 총 병합한다. 
    
        AAAAA = AAAAA + 1 
    
        if AAAAA == 20:
            break
       

# 병합한 후의 새로운 세트 완성 # 새로운 세트를 완성하고 나면 이제 이 세트에 대한 개별 평가 시작 
# New_Set 이거는 그냥 경로일 뿐
    set_number = 0 
    new_distance=[]
    while set_number < 21 : 
    
        Test_set = New_set[set_number]
    
        codes =[]
        wow = 0 
    
        while wow<1000:
            code1, code2 = Test_set[wow], Test_set[wow+1]
            codepoint = l[code1][code2]      # test_set 의 거리 구하는 공식 
            codes.append(codepoint)          # 거리 구함 
            wow = wow + 1 
            if wow == 1000 : 
                break
            
        sum_codes = sum(codes)
    
        new_distance.append(sum_codes)      # 새로운 거리들 
    
        set_number = set_number + 1 
    
        if set_number == 21:    # 거리 6개 구하기 끝 
            break
        
    new_min_number = min(new_distance) # 새로운 거리 중에서 작은 것들 찾기  
    new_minnum = new_distance.index(new_min_number)  # 제일 작은 거리의 위치 
    parent = New_set[new_minnum]
    
    Bignumber = Bignumber + 1 
    if Bignumber == 35000 :
        break 
        
print(new_min_number)
NUMBER = 0 
while NUMBER < 1001 : 
    parent[NUMBER] = parent[NUMBER] + 1
    NUMBER = NUMBER + 1 
    if NUMBER == 1001: 
        print(parent)      #경로 출력 
        
        
f= open("tspoutput33.txt",'w')
f = open("C:/Users/박광서/tspoutput33.txt", 'wt')
f.write("\n" .join(map(lambda x : str(x), parent )))
f.close() 