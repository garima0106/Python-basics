import random 
class Coin:
	def __init__(self, rare=False, clean=True, heads=True,**kargs):
		for key,value in kargs.items():
			setattr(self,key,value)
		
		self.is_rare=rare
		self.is_clean=True
		self.is_heads=heads
		if self.is_rare:
			self.value=self.original_value*1.25
		else:
			self.value=self.original_value
		
		if self.is_clean:
			self.color=self.clean_color
		else:
			self.color=self.rusty_color

	def clean(self):
		self.color=self.clean_color

	def rusty(self):
		self.color=self.rusty_color


	def flip(self):
		head_options=[True,False]
		choice=random.choice(head_options)
		self.heads=choice

	def __del__(self):
		print("Coin Spent!")


class Pound(Coin):

	def __init__(self):
		data={
		"original_value":1.00,
		"clean_color":"gold",
		"rusty_color":"greenish",
		"dia":22.5,
		"thickness":3.5,
		"num_edges":1,
		"mass":9.5}
		super().__init__(**data)
	
coin1=Pound()
print(coin1.color)
print(coin1.is_rare)
print(type(coin1))
print(coin1.value)
coin2=Pound()
print(coin2.value)
print(coin2.is_rare)
