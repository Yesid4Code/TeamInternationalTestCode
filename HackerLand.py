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
        light_scope = []
        for i in range(light[1], light[2] + 1):
            light_scope.append(i)
        lights_ranges.append(light_scope)

    return lights_ranges


def getWhiteLightLength(n, m, lights):
    print(f'n: {n}, m: {m}, Lights: {lights}')
    lights_ranges = getListOfRanges(lights)
    print("Light Ranges       ", lights_ranges)


    # light (smaller number) that is in all arrays.
    light_min = lights_ranges[0][0]
    for i in lights_ranges:
        if light_min < i[0]:
            light_min = i[0]

    # light (largest number) that is in all arrays.
    light_max = lights_ranges[-1][-1]
    for i in reversed(lights_ranges):
        if light_max > i[-1]:
            light_max = i[-1]

    print(f"The range [{light_min}, {light_max}], has", end=": ")

    white_light = [x for x in range(light_min, light_max + 1)]
    # print(f'Location {white_light} receive white light.')
    return (len(white_light))


if __name__ == '__main__':
    n = [5, 5, 5, 5, 5]
    m = [3, 4, 3, 4, 4]

    lights = [
        [[1, 1, 3], [2, 2, 4], [3, 3, 5]], # Sample and Test Case 0 -> range [3, 3]: 1
        [[1, 1, 5], [1, 2, 4], [2, 2, 4], [3, 2, 4]], # Sample and Tast Case 1 -> range [2,4]: 3
        [[1, 1, 2], [2, 2, 3], [3, 3, 4]], # Test Case 2 -> range[]:0
        [[1, 1, 5], [2, 2, 5], [3, 3, 5]], # Explanation case 1 -> range [3, 5]: 3
        [[1, 1, 5], [2, 2, 4], [3, 2, 4]] # 3??
    ]
    i = 0
    for light in lights:
        white_light = getWhiteLightLength(n[i], m[i], light)
        print(white_light, "white lights.")
        i += 1
        print()