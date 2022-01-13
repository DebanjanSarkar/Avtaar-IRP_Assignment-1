"""
Created on Thu Jan 13 09:48:01 2022

@author: Debanjan Sarkar
"""

import datetime
import random

def generate_unique_id(length):
	"""
	This program takes an integer as parameter which will be the length of the returned unique id.
	For best result, the length should be greater than equal to 6, which is appropriate length.
	The id produced by this function will be cryptographically secure, and contains at least some alphabets and numbers, for apt length provided.
	"""
	try:
		length = abs(int(length))
	except:
		print("A unqiue id cannot be created corresponding to the passed argument.")
		return
	num = "0123456789"
	alpha = "qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM"
	id_obj = random.SystemRandom()
	if(length<6):
		if(length==0)
			length+=1
		uid = "".join(id_obj.sample(alpha,length))
		return(uid)
	else
		#length will be divided into two parts randomly and securely : one will be the Number Of Alphabets(NOA), and other will be Number Of Integers(NOI) in the unique id.
		NOA = id_obj.choice( range( length//2 , length-1 ) )
		NOI = length - NOA
		#now NOA number of alphabets and NOI number of integers will be selected randomly from their entire set(alpha and num respec), using loop.
		alpha_list = []
		num_list = []
		for i in range(NOA):
			alpha_list += id_obj.choice(alpha)
		for i in range(NOI):
			num_list += id_obj.choice(num)
		uid = "".join( id_obj.sample( alpha_list+num_list , length ) )
		return(uid)
	