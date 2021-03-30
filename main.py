class Frame:
    def __init__(self, size):
        self.size = size
        self.frames = self.frameCreate(size)

    def __str__(self):
        return_str = []
        for frames in self.frames.keys():
            return_str.append(f'{frames} : {self.frames[frames]}\n')

        return ''.join(return_str)

    @staticmethod
    def frameCreate(s):
        frame_dict = {}
        for i in range(0, s, 1):
            name = f'F{i}'
            frame_dict[name] = ''

        return frame_dict
