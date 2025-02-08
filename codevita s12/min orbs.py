from collections import
defaultdict,deque
def minimum_orbs(recipes,target):
  graph=defaultdict(list)
  for recipe in recipes:
    potion,ingredients=recipe.split('=')
    ingredients=ingredients.split('+')
    for ingredient in ingredients:
      graph[potion].append((ingredient,len(ingredient)-1))
      queue=deque([(target,0)])
      visited={}
      min_orbs=float('inf')
      while queue:
        potion,orbs=queue.popleft()
        if potion in visited:
          continue visited.add(potion)
          min_orbs=min(min_orbs,orbs)
          for neighbor,cost in graph[potion]:
            queue.append((neighbor,orbs+cost))
            return min_orbs
recipes=["awakening=snakefangs+wolfbane","veritaserum=snakefangs+awakening","dargontonic=awakening+veritaserum"]
target_potion="dargontonic"
result=min_orbs(respices,target_potion)
print(result)
        