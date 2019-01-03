from expand import expand
import copy

def a_star_search (dis_map, time_map, start, end):
    path = []
    ansdict = []
    ansdict.append({'cur': start, 'his': [start], 'curdis': getdis(dis_map, start, end), 'pasttime': 0,'sum': getdis(dis_map, start, end) + 0})
    closedlist = {}
    while len(ansdict):
        # resort the ansdict
        ansdict = sorted(ansdict, key=lambda e: e.__getitem__('cur'))
        ansdict = sorted(ansdict, key=lambda e: e.__getitem__('sum'))
        # pop the node with min sum
        currnode = isend(ansdict, end)
        ansdict.remove(currnode)
        # if currnode == end, return path
        if currnode['cur'] == end:
            path = currnode['his']
            break
        # if currnode already in closedlist
        if currnode['cur'] in closedlist.keys():
            if currnode['sum'] >= closedlist[currnode['cur']]:
                continue
            else:
                closedlist[currnode['cur']] = currnode['sum']
        else:
            closedlist[currnode['cur']] = currnode['sum']
        # find the record of dismap
        temp = expand(currnode['cur'],time_map)
        for item in temp:
            if item in currnode['his']:
                continue
            currnode1 = copy.deepcopy(currnode)
            temphis = currnode1['his']
            temphis.append(item)
            tempsum = currnode['pasttime']+ getdis(time_map, currnode['cur'], item)+getdis(dis_map, item, end)
            # if item in closedlist or not
            if item in closedlist.keys() and tempsum >= closedlist[item]:
                continue
            # if item in ansdict（=opencode）or not
            index = -1
            for i in range(0,len(ansdict)):
                if ansdict[i]['cur'] == item:
                    index = i
            # if item is in opencode（ansdict）
            if index != -1:
                # item's sum < opennode's, exchange them
                if tempsum < ansdict[index]['sum']:
                    ansdict[index] = {'cur': item, 'his': temphis, 'curdis': getdis(dis_map, item, end), 'pasttime': currnode['pasttime']+ getdis(time_map, currnode['cur'], item),'sum': tempsum}
                # item's sum >= opennode's, break
                else:
                    continue
            # if item is not in opencode（ansdict）
            else:
                ansdict.append({'cur': item, 'his': temphis, 'curdis': getdis(dis_map, item, end), 'pasttime': currnode['pasttime']+ getdis(time_map, currnode['cur'], item),'sum': tempsum})
    return path

def getdis(dis_map, curNode, nextNode):
    temp = dis_map[curNode]
    dis = temp[nextNode]
    return dis

def isend(ansdict, end):
    tempnode = ansdict[0]
    tempsum = tempnode['sum']
    for item in ansdict:
        if item['sum'] == tempsum and item['cur'] == end:
            return item
    return tempnode