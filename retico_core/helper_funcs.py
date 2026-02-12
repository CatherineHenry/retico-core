def get_first_instance_of_target_grounded_iu(obj, target_iu_objs:list):
    target_attr = 'grounded_in'
    for target_iu_obj in target_iu_objs:
        if isinstance(obj, dict) and target_attr in obj:
            grounded_in_iu = obj[target_attr]
            if isinstance(grounded_in_iu, target_iu_obj):
                return grounded_in_iu
        elif hasattr(obj, '__dict__') and hasattr(obj, target_attr):
            grounded_in_iu = getattr(obj, target_attr)
            if isinstance(grounded_in_iu, target_iu_obj):
                return grounded_in_iu

    # check if dict
    if isinstance(obj, dict) and target_attr in obj:
        return get_first_instance_of_target_grounded_iu(obj[target_attr], target_iu_objs)
    # check if a python obj and if it has the attr
    elif hasattr(obj, '__dict__') and hasattr(obj, target_attr):
        return get_first_instance_of_target_grounded_iu(getattr(obj, target_attr), target_iu_objs)
    # the target IU(s) were not found grounded in the obj
    else:
        raise ValueError(f"Target IU(s) {target_iu_objs} not found grounded in {obj}")
