import heapq

def best_cables_connection(all_cables):
    heapq.heapify(all_cables)
    
    total_costs = 0

    while len(all_cables) > 1:
        first = heapq.heappop(all_cables)
        second = heapq.heappop(all_cables)

        cost = first + second
        total_costs += cost

        heapq.heappush(all_cables, cost)
    
    return total_costs

# тест
heap_of_cables = [2, 5, 8, 1, 3, 5, 9]

min_costs = best_cables_connection(heap_of_cables)

print(f'Найкраще зєднання кабелів: {min_costs}')