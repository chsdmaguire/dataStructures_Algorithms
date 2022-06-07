

input_list = [2, 1, 3, 4, 4, 5, 6, 7]


def get_statistics(input_list):
    sorted_input = sorted(input_list)
    input_length = len(sorted_input)

    mean = sum(sorted_input) / input_length
    middle_idx = (len(sorted_input) - 1) // 2
    median = sorted_input[middle_idx]

    if input_length % 2 == 0:
        middle_num1 = sorted_input[middle_idx]
        middle_num2 = sorted_input[middle_idx + 1]
        median = (middle_num1 + middle_num2) / 2

    number_counts = {x: sorted_input.count(x) for x in set(sorted_input)}
    mode = max(number_counts.keys(),
               key=lambda unique_number: number_counts[unique_number])

    sample_var = sum([(number - mean) ** 2 / (input_length - 1)
                     for number in sorted_input])

    sample_std = sample_var ** .5

    stand_error = sample_std / input_length ** .5
    z_score_stand_error = 1.96 * stand_error
    confidence_interval = [
        mean - z_score_stand_error, mean + z_score_stand_error]

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_var,
        "sample_standard_deviation": sample_std,
        "mean_confidence_interval": confidence_interval
    }


stats = get_statistics(input_list)
