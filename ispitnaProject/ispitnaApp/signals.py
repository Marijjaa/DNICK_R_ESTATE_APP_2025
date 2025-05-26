from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from ispitnaApp.models import RealEstate, RealEstateAgent, RealEstateCharacteristic


@receiver(pre_save, sender=RealEstate)
def handling_saving_house(sender, instance, **kwargs):
    old_instance = sender.objects.filter(pk=instance.pk).first()
    if old_instance:
        if old_instance.is_bought != instance.is_bought:
            agents_real_estate = RealEstateAgent.objects.filter(real_estate=old_instance).all()
            for agent_real_estate in agents_real_estate:
                agent = agent_real_estate.agent
                agent.number_of_sales += 1
                agent.save()


@receiver([post_save, post_delete], sender=RealEstateCharacteristic)
def handling_saving_character(sender, instance, **kwargs):
    all_chars = sender.objects.filter(real_estate=instance.real_estate).all()
    if all_chars:
        real_estate = all_chars[0].real_estate
        real_estate.characteristic = ", ".join(char.characteristic.name for char in all_chars)
        real_estate.save()
        print("Updated characteristics:", real_estate.characteristic)
