"""
user : Jean TROUSSIER
Date : Jeudi 19 septembre
Obj : multiplication matriciel (fichier principal)
"""
def Are_they_matrix(mat):
    """
    fonction qui verifie que les matrices (liste ici) ait le même nombre d'élément sur chaque ligne
    """
    try :
        valligne = len(mat[0])
    except:
        return False
    for i in mat:
        try :
            if valligne != len(i) : 
                return False
            for j in i:
                int(j)
        except:
            return False
    return True



def mult_possible(MatA,MatB):
    """
    fonction qui reçoit deux matrice et qui renvoie true si les matrice sont divisible entre elle sinon false
    """
    if len(MatA) != len(MatB):
        return False
    return True

def multiplication(MatA, MatB):
    """
    ce programme prend en entrée deux matrice a multiplier et return la dite matrice 
    """
    resultat_matrice = []
    conteneur = []
    number = 0
    for i in range(len(MatA)):
        for k in range(len(MatB[0])):
            for j in range(len(MatA[0])):
                number += MatA[i][j] * MatB[j][k]
            conteneur.append(number)
            number = 0
        resultat_matrice.append(conteneur[:])
        conteneur = []
    return resultat_matrice
