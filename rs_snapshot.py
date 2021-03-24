import pyrealsense2.pyrealsense2 as rs
#import pyrealsense2 as rs
import numpy as np
import time

def take_snapshot():
    pipeline = rs.pipeline()    
    config = rs.config()
    config.enable_stream(stream_type=rs.stream.depth, width=640, height=480, format=rs.format.z16, framerate=30)
    pipeline.start(config)

    #colorizer = rs.colorizer()

    cnt = 0

    try:
        while True:
            frames = pipeline.wait_for_frames()
            cnt += 1
            if cnt > 10:
                #colorized = colorizer.process(frames)

            
                depth_frame = frames.get_depth_frame()         
            
                if not depth_frame:
                    continue

                print("Get depth frame")

                currentTime = time.time()
                filename = 'snapshot_' + str(currentTime) + '.ply'
                ply = rs.save_to_ply(filename)
                ply.set_option(rs.save_to_ply.option_ply_binary, False)
                ply.set_option(rs.save_to_ply.option_ignore_color, True)
                ply.set_option(rs.save_to_ply.option_ply_normals, False)
                ply.set_option(rs.save_to_ply.option_ply_mesh, False)
                print("Saving point cloud")
                ply.process(depth_frame)
                #ply.process(colorized)
                print("Point cloud is created as {}".format(filename))

                pipeline.stop()
                return filename
                
                #depth_image = np.asanyarray(depth_frame.get_data())
                #print(depth_image.shape)
                #np.savetxt('rs_depth_image.ply', depth_image, fmt= '%.6e', delimiter=' ', newline='\n')
                break
    except:
        print("error occurred")
        pipeline.stop()
            
    #finally:
    #    pipeline.stop()
    #    print("Pipeline finished")


if __name__ == '__main__':
    out_file = take_snapshot()
