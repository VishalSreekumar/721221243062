from rest_framework.decorators import api_view
from rest_framework.response import Response 


listOfNumbers = []
@api_view(['GET','POST'])
def calculator(request):
    if request.method == "POST":
        b1 = False
        data = list(set((request.data)["numbers"]))
        listOfNumbers.append(list(data))
        if  len(listOfNumbers) > 1:
            b1 = True
        if b1 == False:
            prevState = []
        else:
            prevState = list(listOfNumbers[-2])
        if len(listOfNumbers) == 0:
            average = 0
        else:
            average = sum(list([int(i) for i in list(data)]))//len(list(data))
        finalOutput = {
            "numbers" : list(data),
            "windowPrevState": prevState,
            "windowCurrState":sorted(list(data)),
            "avg" : average

        }
        print(listOfNumbers)
        return Response(finalOutput)
    else:
        return Response(listOfNumbers)
