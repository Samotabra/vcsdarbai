import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# # Sachmatu lenta
#
# # kuriam lenta
# board = [
#     ['r','n','b','q','k','b','n','r'],
#     ['p','p','p','p','p','p','p','p'],
#     [' ',' ',' ',' ',' ',' ',' ',' '],
#     [' ',' ',' ',' ',' ',' ',' ',' '],
#     [' ',' ',' ',' ',' ',' ',' ',' '],
#     [' ',' ',' ',' ',' ',' ',' ',' '],
#     ['P','P','P','P','P','P','P','P'],
#     ['R','N','B','Q','K','B','N','R']
#
# ]
#
# def display_board(board):
#     print("  a b c d e f g h")
#     print("  ----------------")
#     for i, row in enumerate(board, start=1):
#         print(f"{i} |{' '.join(row)}|")
#     print("  ----------------")
#
# def is_valid_move(board, start, end):
#     piece = board[start[0]][start[1]]
#     if piece == ' ':
#         return False
#     if start == end:
#         return False
#     if not (0 <=start[0] < 8 and 0 <= start[1] < 8 and 0 <= end[0] < 8 and 0 <=end[1] <8):
#         return False
#     return True
#
# def make_move(board, start, end):
#     piece = board[start[0]][start[1]]
#     board[start[0]][start[1]] = ' '
#     board[end[0]][end[1]] = piece  # figuros pradine padetis
#
# def is_game_over(board):
#     return False
#
#
# while True:
#     display_board(board)
#     start = input("Startine pozicija (pvz: 'a2'): ")
#     end = input("Ejimo kombinacija (pvz: 'b3'): ")
#     start = (int(start[1]) - 1, ord(start[0]) - ord('a'))
#     end = (int(end[1]) - 1, ord(end[0]) - ord('a'))
#     if is_valid_move(board, start, end):
#         make_move(board, start, end)
#         if is_game_over(board):
#             display_board(board)
#             print("Game over")
#             break
#     else:
#         print("Invalid move, please try again")
#
#
#
# if __name__=='__main__':
#     display_board(board)

# automatinis duomenu analizavimas
def load_data(file):
    data = pd.read_csv(file, encoding='utf-8')
    return data
def clean_data(data):
#     cleaned_data = data.drop_duplicates()
#     cleaned_data['amzius'] = cleaned_data['amzius'].astype(int)
#     cleaned_data['vardas'] = cleaned_data['vardas'].str.strip()
#     cleaned_data['pavarde'] = cleaned_data['pavarde'].str.replace(' ','')
#
     cleaned_data = data.dropna()
     return cleaned_data

def perform_calculation(data):
    calculations = {}
    calculations['average age'] = data['amzius'].mean()
    calculations['age range'] = np.ptp(data['amzius'])  # ptp iesko range (grazins intervala tarp didziausio ir maziausio)
    return calculations

def visualize_data(data):

    age_counts = data['amzius'].value_counts().sort_index()

    plt.figure(figsize=(10,6))
    plt.bar(age_counts.index, age_counts.values)
    plt.xlabel('amzius')
    plt.ylabel('pasikartojimai')
    plt.title('pasiskirstymai pagal amziu')
    plt.show()

def main():
    file_path = "duomenys.csv"
    data = load_data(file_path)
    cleaned_data = clean_data(data)
    calculations = perform_calculation(cleaned_data)

    print('Skaiciavimai: ')
    for key, value in calculations.items():
        print(f'{key}: {value}')

    visualize_data(cleaned_data)

if __name__=='__main__':
    main()













