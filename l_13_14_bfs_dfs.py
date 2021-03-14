# mapL=[[0,1,1,1,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,0,0,0,1,0,0,1,0,0], [0,0,0,1,0,1,1,0,0,0],[0,0,0,0,1,0,1,1,1,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,1,0],[0,0,0,0,0,1,0,1,0,1],[0,0,0,0,0,0,0,0,1,0]]

def bfs(mapL, start):

	v_p_l = []
	
	for i in range(0, len(mapL)):
		v_p_l.append([-1, -1])
	
	print(v_p_l)
	
	queue = [start]
	# parent  and level. visited is considered as the position 
	v_p_l[start][0] = ''
	v_p_l[start][1] = 0
	

	while queue != []:
		i = queue.pop()
		for j in range(0, len(mapL[i])):
			if mapL[i][j] == 1:
				if v_p_l[j][1] == -1:
					queue.append(j)
					v_p_l[j][0] = i			# parent 
					v_p_l[j][1] = v_p_l[i][1]  + 1  # level

	print(v_p_l)

def dfscall(mapL, start):
	
	v_p_l = []
	for i in range(0, len(mapL)):
		v_p_l.append([-1, -1])

	dfs(mapL, start, v_p_l)
	print(v_p_l)
	

def dfs(mapL, start, v_p_l):
	
	v_p_l[start][0] = 1
	
	for i in range(0, len(mapL)):
		if v_p_l[i][0] == -1:
			v_p_l[i][1] = start
			dfs(mapL, i, v_p_l)
