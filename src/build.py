import os
import argparse

import textwrap
from  MosaicImage import MosaicImage
from TileProcessor import TileProcessor
from TargetImage import TargetImage
from TileFitter import TileFitter
from SystemUtils import  Welcome
from termcolor import colored
from multiprocessing import Process, Queue, cpu_count


__version__ = '1.0001b'




def logo():
    s ="""  
 _____ ______   ________  ________          _____ ______   ________  ________  ________  ___  ________     
|\   _ \  _   \|\   __  \|\_____  \        |\   _ \  _   \|\   __  \|\   ____\|\   __  \|\  \|\   ____\    
\ \  \\\__\ \  \ \  \|\  \|____|\ /_       \ \  \\\__\ \  \ \  \|\  \ \  \___|\ \  \|\  \ \  \ \  \___|    
 \ \  \\|__| \  \ \   ____\    \|\  \       \ \  \\|__| \  \ \  \\\  \ \_____  \ \   __  \ \  \ \  \       
  \ \  \    \ \  \ \  \___|   __\_\  \       \ \  \    \ \  \ \  \\\  \|____|\  \ \  \ \  \ \  \ \  \____  
   \ \__\    \ \__\ \__\     |\_______\       \ \__\    \ \__\ \_______\____\_\  \ \__\ \__\ \__\ \_______\\
    \|__|     \|__|\|__|     \|_______|        \|__|     \|__|\|_______|\_________\|__|\|__|\|__|\|_______|
                                                                       \|_________|                        
                                                                                              
     """

    return colored(s, 'white')


def licence():
    s = """
/*
 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE" (Revision 44):
 * <gregorio.flores@aniachitech.com> wrote this script.  
 * As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a beer in return. 
 * or give back something to the world, like give food to homeless dog. 
 * Sincerely Gregorio Flores 
 * ----------------------------------------------------------------------------
 */
    """

    return colored(s, 'white')







def quitting():
    print('Quitting......')
    quit(-1)


def validateParameters(args):


    if not os.path.isfile(args['image']):
        print('File:',colored((args['image']),'red'),'not found please verify.')
        quitting()
    elif not os.access(args['image'], os.R_OK):
        print('File:', colored((args['image']), 'red'), 'can not be read')
        quitting()
    elif not os.path.isdir(args['mp3_dir']):
        print('Directory:', colored((args['mp3_dir']), 'red'), 'does not exists')
        quitting()
    elif not os.access(args['mp3_dir'], os.R_OK):
        print('Directory:', colored((args['mp3_dir']), 'red'), 'can not be read')
        quitting()
    elif args['tmr'] not in list(range(2,11)):
        print(colored((args['tmr']), 'red'), 'is an invalid parameter for tile matching resolution. Use 2 to 10')
        quitting()
    elif args['enl'] not in [2,4,8,10]:
        print( colored((args['enl']), 'red'), 'is an invalid parameter for enlargement factor. Use 2, 4, 8 or 10')
        quitting()
    elif args['tsize'] not in [10,30,40,50,60,70,80,90,100]:
        print('Value:', colored((args['tsize']), 'red'), 'is an invalid parameter. Use 10 20 30 40 50 60 .. 100')
        quitting()




def parseInitParameters():


    ap = argparse.ArgumentParser( description=textwrap.dedent(logo()), formatter_class=argparse.RawDescriptionHelpFormatter)



    ap.add_argument('-image', required=True, help='The image to be processed ', type=str )
    ap.add_argument('-mp3_dir', required=True, help='The mp3 library directory', type=str)
    ap.add_argument('-output', required=False, help='Output file name', type=str, default='output.jpg')
    ap.add_argument('-enl', required=False, help='enlargement factor ' , type=int, default=8)
    ap.add_argument('-tmr', required=False, default='5', type=int,  help='tile matching resolution (higher values give better fit but require more processing) from 2 to 10 the default is 5', )
    ap.add_argument('-tsize', required=False, default='50', type=int,  help='tile box size from 20 to 100. Default value is 50' )

    args = vars(ap.parse_args())
    validateParameters(args)

    return args



"""


"""

def build_mosaic(result_queue, all_tile_data_large, mosaic,workers,outfile):
    #mosaic = MosaicImage(original_img_large)

    active_workers = workers
    while True:
        try:
            img_coords, best_fit_tile_index = result_queue.get()

            if img_coords == None:
                active_workers -= 1
                if not active_workers:
                    break
            else:

                if (best_fit_tile_index == None):
                    #tile_data = all_tile_data_large[0]
                    #mosaic.add_tile(tile_data, img_coords)
                    # todo fix
                    pass
                else:

                    tile_data = all_tile_data_large[best_fit_tile_index]
                    mosaic.add_tile(tile_data, img_coords)

        except KeyboardInterrupt:
            pass

    mosaic.save(outfile)
    print ('\nFinished, output is in', outfile)



"""

"""

def fit_tiles(work_queue, result_queue, tiles_data):
    # this function gets run by the worker processes, one on each CPU core
    tile_fitter = TileFitter(tiles_data)

    while True:
        try:
            img_data, img_coords = work_queue.get(True)
            if img_data == None:
                break
            tile_index = tile_fitter.get_best_fit_tile(img_data)
            result_queue.put((img_coords, tile_index))
        except KeyboardInterrupt:
            pass

    # let the result handler know that this worker has finished everything
    result_queue.put((None, None))

"""


"""

def compose_mosaic(original_img, tiles,workers,args):
    original_img_large, original_img_small = original_img
    tiles_large, tiles_small = tiles

    mosaic = MosaicImage(original_img_large,args['tsize'])

    all_tile_data_large = list(map(lambda tile: list(tile.getdata()), tiles_large))
    all_tile_data_small = list(map(lambda tile: list(tile.getdata()), tiles_small))


    work_queue = Queue(workers)
    result_queue = Queue()

    try:
        # start the worker processes that will build the mosaic image
        Process(target=build_mosaic, args=(result_queue, all_tile_data_large, mosaic,workers,args['output'])).start()

        # start the worker processes that will perform the tile fitting
        for n in range(workers):
            Process(target=fit_tiles, args=(work_queue, result_queue, all_tile_data_small)).start()

        lsize = mosaic.x_tile_count * mosaic.y_tile_count
        tile_block_size = args['tsize'] / max(min(args['tmr'], args['tsize']), 1)
        i=0
        for x in range(int(mosaic.x_tile_count)):
            for y in range(int(mosaic.y_tile_count)):
                large_box = (x * args['tsize'], y * args['tsize'], (x + 1) * args['tsize'], (y + 1) * args['tsize'])
                small_box = (
                x * args['tsize'] / tile_block_size, y * args['tsize'] / tile_block_size, (x + 1) * args['tsize'] / tile_block_size,
                (y + 1) * args['tsize'] / tile_block_size)
                work_queue.put((list(original_img_small.crop(small_box).getdata()), large_box))
                i+=1
                Welcome.showAdvance('Workinbg on:',total=lsize,i=i,outMessage=' Done')

    except KeyboardInterrupt:
        print ('\nHalting, saving partial image please wait...')

    finally:
        # put these special values onto the queue to let the workers know they can terminate
        for n in range(workers):
            work_queue.put((None, None))




"""
this is the main entry point to the application
first we need to validate all input data
"""


if __name__ == '__main__':
    os.system('clear')
    print(licence())
    args = parseInitParameters()
    Welcome.printWelcome(logo(),color_d='white')
    Welcome.printValues(args,color_d='white')
    tiles_data =TileProcessor(args['mp3_dir'],args['tsize'],args['tmr']).get_tiles()
    image_data = TargetImage(args['image'],args['tsize'],args['enl'],args['tmr']).get_data()
    workers = max(cpu_count() - 1, 1)
    compose_mosaic(image_data, tiles_data,workers,args)










