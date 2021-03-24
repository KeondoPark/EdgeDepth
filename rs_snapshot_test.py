#import pyrealsense2.pyrealsense2 as rs
import pyrealsense2 as rs
import numpy as np
import time

def take_snapshot():
    pipeline = rs.pipeline()    
    config = rs.config()
    W = 640
    H = 480
    config.enable_stream(stream_type=rs.stream.any, width=W, height=H, format=rs.format.z16, framerate=30)
    pipeline.start(config)
    #pipeline.start()

    cnt = 0

    #try:
    while True:
        frames = pipeline.wait_for_frames()
        cnt += 1
        if cnt > 10:
            depth_frame = frames.get_depth_frame()

            if not depth_frame:
                continue            
            print("1")
            point_cloud = rs.pointcloud()
            print("2")
            points = point_cloud.calculate(depth_frame)
            print("3")
            verts = np.asanyarray(points.get_vertices()).view(np.float32).reshape(-1, W, 3)  # xyz            

            print("4")
            currentTime = time.time()
            print(verts.shape)
            print(verts[:20])

            points.export_to_ply("PC_Test.ply", depth_frame)
            print("Original points exported")

            #color_frame = frames.get_color_frame()
            #depth_to_color_extrin = depth_frame.profile.get_extrinsics_to(color_frame.profile)

            #print(depth_to_color_extrin)
            #print('Rotation')
            #print(depth_to_color_extrin.rotation)
            #print('Translation')
            #print(depth_to_color_extrin.translation)
            #for i in range(len(points)):
            #    color_point = rs.rs2_transform_point_to_point(depth_to_color_extrin, points[i])



            #filename = 'snapshot_' + str(currentTime) + '.ply'
            #ply = rs.save_to_ply(filename)
            #ply.set_option(rs.save_to_ply.option_ply_binary, False)



            #print("Saving point cloud")
            #ply.process(depth_frame)
            #print("Point cloud is created as {}".format(filename))
         



            break
    #except:
    #    print("error occurred")
    #    pipeline.stop()
            
    #finally:
    #    pipeline.stop()

    print(cnt)



if __name__ == '__main__':
    take_snapshot()
