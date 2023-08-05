from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def connect4_board(request):
    # Your logic to set up the Connect 4 board goes here
    # For simplicity, we'll just create an empty 6x7 board using a list of lists
    rows = 6
    cols = 7
    board = [['' for _ in range(cols)] for _ in range(rows)]

    return render(request, 'connect4_board.html', {'board': board})