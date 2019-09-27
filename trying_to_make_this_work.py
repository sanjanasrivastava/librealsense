import pyrealsense2 as rs


try:
  pipeline = rs.pipeline()
  pipeline.start()

  while True:
    frames = pipeline.wait_for_frames()
    depth = frames.get_depth_frame()
    if not depth: continue

    width, height = depth.get_width(), depth.get_height()
    dist_to_center = depth.get_distance(width // 2, height // 2)
    print('The camera is facing an object % meters away' % dist_to_center)

except Exception as e:
  print(e)
  pass
