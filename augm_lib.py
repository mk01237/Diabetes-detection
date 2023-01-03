import Augmentor
p = Augmentor.Pipeline("data")
p.rotate(probability=1, max_left_rotation=25, max_right_rotation=25)
p.zoom(probability=1, min_factor=1.1, max_factor=1.5)
p.sample(65)
p.process()
