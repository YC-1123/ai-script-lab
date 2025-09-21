def should_trigger_conflict(messages: list) -> bool:
    """
    冲突触发规则：任意角色提及质疑、对立情绪词则触发冲突
    """
    trigger_words = ["不信", "怀疑", "隐瞒", "骗", "意图", "威胁"]
    for msg in messages:
        if any(word in msg for word in trigger_words):
            return True
    return False


def should_trigger_understanding(messages: list) -> bool:
    """
    理解触发规则：双方提及“理解”、“原谅”或类似词语
    """
    key_words = ["理解", "原谅", "接受", "信任", "误会"]
    return all(any(word in msg for word in key_words) for msg in messages)