import PIL, argparse, random
from PIL import ImageFilter, Image
parser = argparse.ArgumentParser(description='An automatic image deepfryer. [Put an image named "file.jpeg" into the same directory as the program]')
parser.add_argument('Reps', metavar='Reps', type=int, nargs=1 ,help='Number of times to repeat filters and save as JPEG. [Must be greater than 0]')
parser.add_argument('Quality', metavar='Quality', type=int, nargs=1 ,help='JPEG quality level. [Must range from 1 to 100]')
parser.add_argument('--Preset1' ,help='Applies preset #1.', action='store_true')
parser.add_argument('--Preset2' ,help='Applies preset #2.', action='store_true')
parser.add_argument('--Preset3' ,help='Applies preset #3.', action='store_true')
parser.add_argument('--Preset4' ,help='Applies preset #4.', action='store_true')
parser.add_argument('--PresetAll' ,help='Applies preset #1.', action='store_true')
args = parser.parse_args()
Reps, Quality = args.Reps[0], args.Quality[0]
for a in range(Reps):
	im = Image.open(r'file.jpeg')
	im = im.convert("RGB")
	if args.Preset1:
		b=[10565, 45549, -67901, -46799, -57560, -64673, -52895, -31584, 25037, 66427, -38855, 72928, -21056, -55236, 88961, -24615, 51251, -57564, 95122, 13710, 3470, 25518, 22741, -26711, 32880]
		im = im.filter(PIL.ImageFilter.Kernel((5,5),b))
	if args.Preset2:
		b=[-42769, -47366, -6327, -59902, 63094, -69054, -91416, 36987, 70388, -3458, 64161, -65908, 79106, 49140, 77962, -85455, 76052, 62467, 92296, -40580, -97732, 67348, -40653, 1071, -25043]
		im = im.filter(PIL.ImageFilter.Kernel((5,5),b))
	if args.Preset3:
		b=[-93348, -44913, -27314, 61643, 97373, -6806, -98148, 50149, -7899, 96194, -46385, -94996, -23990, 62162, 26812, 16686, 1009, 71703, 21549, -38508, -81769, -18591, 85337, -33170, 2318]
		im = im.filter(PIL.ImageFilter.Kernel((5,5),b))
	if args.Preset4:
		b=[-88302, 46628, 88249, -60649, 24986, -77134, 50971, 26063, 58189, 10676, -89626, 18, 70666, -62326, 93465, -60105, 35867, 4451, -15156, 13026, -66009, 84993, 39452, -31695, -87723]
		im = im.filter(PIL.ImageFilter.Kernel((5,5),b))
		b=[686, 35748, 53498, 75567, -700, -22310, 92494, 5821, 66711, -80238, -10783, 87038, -83272, 9760, -34346, -13192, 82088, -66142, -23462, 95482, 19596, -46091, -82367, -51061, -85617]
		im = im.filter(PIL.ImageFilter.Kernel((5,5),b))
	if args.PresetAll:
		b=[10565, 45549, -67901, -46799, -57560, -64673, -52895, -31584, 25037, 66427, -38855, 72928, -21056, -55236, 88961, -24615, 51251, -57564, 95122, 13710, 3470, 25518, 22741, -26711, 32880]
		im = im.filter(PIL.ImageFilter.Kernel((5,5),b))
		b=[-42769, -47366, -6327, -59902, 63094, -69054, -91416, 36987, 70388, -3458, 64161, -65908, 79106, 49140, 77962, -85455, 76052, 62467, 92296, -40580, -97732, 67348, -40653, 1071, -25043]
		im = im.filter(PIL.ImageFilter.Kernel((5,5),b))
		b=[-93348, -44913, -27314, 61643, 97373, -6806, -98148, 50149, -7899, 96194, -46385, -94996, -23990, 62162, 26812, 16686, 1009, 71703, 21549, -38508, -81769, -18591, 85337, -33170, 2318]
		im = im.filter(PIL.ImageFilter.Kernel((5,5),b))
		b=[-88302, 46628, 88249, -60649, 24986, -77134, 50971, 26063, 58189, 10676, -89626, 18, 70666, -62326, 93465, -60105, 35867, 4451, -15156, 13026, -66009, 84993, 39452, -31695, -87723]
		im = im.filter(PIL.ImageFilter.Kernel((5,5),b))
		b=[686, 35748, 53498, 75567, -700, -22310, 92494, 5821, 66711, -80238, -10783, 87038, -83272, 9760, -34346, -13192, 82088, -66142, -23462, 95482, 19596, -46091, -82367, -51061, -85617]
		im = im.filter(PIL.ImageFilter.Kernel((5,5),b))
	im.save('file.jpeg', "JPEG", quality=Quality)
