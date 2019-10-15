def is_overlapping(rectangleA,rectangleB):
	"""
	Function to check if two rectangles overlap
	based on their boundingboxes.
	The function accepts two types of boundingBoxes.
	Either an 8 point boundingBox or a 4 point BoundingBox.
	8 point boundingbox format : [x1,y1,x2,y2,x3,y3,x4,y4]
	4 point boundingbox format : [x1,y1,x3,y3]
	"""
	if len(rectangleA) == (rectangleB) == 8:
		x1,y1,x2,y2,x3,y3,x4,y4 = rectangleA
		X1,Y1,X2,Y2,X3,Y3,X4,Y4 = rectangleB
	elif len(rectangleA) == len(rectangleB) == 4:
		x1,y1,x3,y3 = rectangleA
		X1,Y1,X3,Y3 = rectangleB
	else:
		print("Wrong boundingBox Format")
		return False
	# If one rectangle is on left side of other 
	if x1 > X3 or X1 > x3 :
		return False

	# If one rectangle is above other
	if y1 > Y3 or Y1 > y3:
		return False

	return True