class ExercisePlan:
    autoincremented_id = 1

    def __init__(self, trainer_id, equipment_id, duration):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.autoincremented_id
        ExercisePlan.autoincremented_id += 1

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        hours_to_minutes = hours * 60
        return cls(trainer_id, equipment_id, hours_to_minutes)

    @staticmethod
    def get_next_id():
        return ExercisePlan.autoincremented_id

    def __repr__(self):
        return f'Plan <{self.id}> with duration {self.duration} minutes'
