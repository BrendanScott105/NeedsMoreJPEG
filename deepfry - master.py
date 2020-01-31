import PIL, argparse, random
from PIL import ImageFilter, Image
parser = argparse.ArgumentParser(description='An automatic meme deepfryer. [Put an image named "file.jpeg" into the same directory as the program to fry the image]')
parser.add_argument('Reps', metavar='Reps', type=int, nargs=1 ,help='Number of times to repeat filters and save as JPEG. [Must be greater than 0]')
parser.add_argument('Quality', metavar='Quality', type=int, nargs=1 ,help='JPEG quality level. [Must range from 1 to 100]')
parser.add_argument('ConMtrRnge', metavar='ConMtrRnge', type=int, nargs=1 ,help='Range of convolution matrix values.')
parser.add_argument('--kernel' ,help='Applies a random 3x3 convolution matrix for every repetition.', action='store_true')
args = parser.parse_args()
Reps, Quality, kernel, ConMtrRnge = args.Reps[0], args.Quality[0], args.kernel, args.ConMtrRnge[0]
for a in range(Reps):
	im = Image.open(r'file.jpeg')
	im = im.convert("RGB")
	print(a,end='\r')
	if kernel:
		b=[random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge),random.randint(-ConMtrRnge,ConMtrRnge)]
		im = im.filter(PIL.ImageFilter.Kernel((5,5),b))
	im.save('file.jpeg', "JPEG", quality=Quality)