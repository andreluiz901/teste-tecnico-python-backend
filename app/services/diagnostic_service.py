from app.models.focus_log import FocusLog


def generate_productivity_diagnostic(
    focus_logs: list[FocusLog]
):
    if not focus_logs:
        return {
            "media_foco": 0,
            "tempo_total_focado": 0,
            "feedback": "Nenhum registro encontrado.",
            "padroes_detectados": []
        }

    total_focus = sum(
        log.nivel_foco for log in focus_logs
    )

    total_time = sum(
        log.tempo_minutos for log in focus_logs
    )

    average_focus = round(
        total_focus / len(focus_logs),
        2
    )

    feedback = generate_feedback(
        average_focus
    )

    patterns = generate_patterns(
        focus_logs,
        average_focus
    )

    return {
        "media_foco": average_focus,
        "tempo_total_focado": total_time,
        "feedback": feedback,
        "padroes_detectados": patterns
    }

def generate_patterns(
    focus_logs: list[FocusLog],
    average_focus: float
):
    patterns = []

    if average_focus >= 4:
        patterns.append(
            "Você mantém um padrão consistente "
            "de alta concentração."
        )

    high_interruption_logs = [
        log for log in focus_logs
        if log.interrupcoes >= 3
    ]

    if high_interruption_logs:
        patterns.append(
            "Sessões com muitas interrupções "
            "parecem impactar seu foco."
        )

    long_sessions = [
        log for log in focus_logs
        if log.tempo_minutos >= 120
    ]

    if long_sessions:
        patterns.append(
            "Sessões muito longas podem "
            "reduzir sua eficiência mental."
        )

    category_focus = {}

    for log in focus_logs:
        if log.categoria not in category_focus:
            category_focus[log.categoria] = []

        category_focus[log.categoria].append(
            log.nivel_foco
        )

    best_category = None
    best_average = 0

    for category, values in category_focus.items():
        avg = sum(values) / len(values)

        if avg > best_average:
            best_average = avg
            best_category = category

    if best_category:
        patterns.append(
            f"A categoria '{best_category}' "
            "apresenta seu melhor desempenho."
        )

    return patterns


def generate_feedback(
    average_focus: float
):
    if average_focus < 3:
        return (
            "Seu nível de foco está baixo. "
            "Considere reduzir distrações "
            "e realizar pausas estratégicas."
        )

    if average_focus < 4:
        return (
            "Seu foco está razoável, "
            "mas ainda há espaço para melhorar "
            "a consistência das sessões."
        )

    return (
        "Você está em um excelente ritmo "
        "de produtividade e concentração."
    )