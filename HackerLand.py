#!/bin/python3


from itertools import count


def getListOfRanges(lights):
    '''function that gets a list with the locations of the lights.
    lights: 2D_Integer_array.
    Return:
        2D_Integer_Array lights
    '''
    lights_ranges = []

    for light in lights:
        light_range = []
        for i in range(light[1], light[2] + 1):
            light_range.append(i)
        lights_ranges.append(light_range)

    return lights_ranges


def getWhiteLightLength(n, m, lights):

    lights_ranges = getListOfRanges(lights)
    print(lights_ranges)


    # light (smaller number) that is in all arrays.
    light_min = lights_ranges[0][0]
    for i in lights_ranges:
        if light_min < i[0]:
            light_min = i[0]

    # light (largest number) that is in all arrays.
    light_max = lights_ranges[0][-1]
    for i in lights_ranges:
        if light_max not in i:
            return 0

    print(f"The range [{light_min}, {light_max}]")

    white_light = [x for x in range(light_min, light_max + 1)]
    print(f'Location {white_light} receive white light.')
    return (len(white_light))


if __name__ == '__main__':
    n = 5
    m = 3

    lights = [
        [[1, 1, 3], [2, 2, 4], [3, 3, 5]],
        [[1, 1, 5], [2, 2, 5], [3, 3, 5]]
    ]
    for light in lights:
        white_light = getWhiteLightLength(n, m, light)
        print(white_light)