def displayIndexRating(restaurant, index):
    """This function will the rating at the specified index within the specified restaurant's list.  This function also takes in one mutable, argument which is stored into restaurant, and one immutable argument which is stored into index.""" 

    #printing rating at specified restaurant and index to user
    print("User: " + restaurant.getRatings(index).getUser())
    print("Rating Value: " + str(restaurant.getRatings(index).getRatingValue()))
    print("Comment: " + restaurant.getRatings(index).getComment() + "\n")