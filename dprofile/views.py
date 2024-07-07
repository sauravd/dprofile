from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import HhSurvey
from folium.plugins import TagFilterButton
from folium.plugins import Search
import folium
import geopandas
import os
import numpy as np
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
from plotly.offline import plot
from plotly.graph_objs import Bar, Pie
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine
from .models import AccessToRoadnetwork, AgriLivstkCooperatives, \
    AnimalHusbandryFirms, AnimalProducts, AvailabilityOfIrrigationFacilities, \
    BuildingSlumHousingForUnderprivileged, CitizenAwarenessVillageDevelpmtOrg, \
    CommunityInstitutionDetails, DeadFamilyMembers, DescriptionOfBridges, \
    DescriptionOfCommunityForests, DescriptionOfDiseaseTreatment, \
    DescriptionOfGovernmentBuilding, DetailsOfNgo, DisasterManagement, \
    EnvironmentAndHygiene, FarmersEntrepreneursAndSavingsGroups, \
    FinancialInstutionsDetails, ForestDescription, ForestInLocalLevel, \
    ForestryAndEnvironment, GenderEqualtiyNSocialInclusion, \
    GhattaMillsAndCollectionProcessingCenters, GovernmentOfficesAndAgencies, \
    HealthNNutritionInformation, HotelsLodgesResturantsHomestay, HrRelatedToAgricultureAndAnimalHusbandry, \
    InvestmentInformation, LandUseCondition, LoanInformation, MajorFestivalsAndFairs, MappingOfNaturalResources, \
    MotherWomenGroupAndTraditionalGroup, NaturalCalamity, PersonalEventDetails, ProjectsOfPride, \
    PublicAndCommunityBuildings, PublicPondsAndFisheries, PublicServiceDelivery, Roadways, \
    SavingsInformation, SocialSecurityProgramDetails, SolidWasteManagement, SourceOfAirPollution, YearlyCultivation



class HomePageView(TemplateView):
    template_name = 'index.html'

# def HomePageView(request):
#     return render(request,'dprofile/index.html')




def PersonalEventDetails(request):
    queryset = PersonalEventDetails.objects.all()
    alchemyEngine = create_engine('postgresql://postgres:PostGRE@127.0.0.1:5432/digitalpalika')
    conn = alchemyEngine.connect()
    # conn = psycopg2.connect(database='hatuwagadi', user="postgres", password="PostGRE", host="127.0.0.1", port="5432")
    query1 = "select * from personal_event_details;"
    df1 = pd.read_sql_query(query1, con=conn)
    layout = go.Layout(barmode='group')
    # config = {'displayModeBar': False}
    config = {'displaylogo': False}
    fig1 = plot(px.bar(df1, x='count', y='birth',
                       title='व्यक्तिगत घटना विवरण '), output_type='div', config=config, image_height=100)
    fig2 = plot(px.bar(df1, x='count', y='death'), output_type='div', config=config, image_height=100)
    fig3 = plot(px.bar(df1, x='count', y='marriage'), output_type='div', config=config, image_height=100)
    fig4 = plot(px.bar(df1, x='count', y='divorce'), output_type='div', config=config, image_height=100)
    fig5 = plot(px.bar(df1, x='count', y='migration_incoming'), output_type='div', config=config, image_height=100)
    fig6 = plot(px.bar(df1, x='count', y='migration_outgoing'), output_type='div', config=config, image_height=100)
    # fig1 = plot(df1.plot())
    # fig1 = px.pie(df1, values='road_infrastructure', names='road_infrastructure_condition',title='सडक सञ्जालमा पहुँच', height=300)
    # piechart = fig1.to_html(full_html=False, include_plotlyjs=False)
    conn.close()
    return render(request, "dprofile/personaleventdetails.html", context={'queryset': queryset, "fig1": fig1,
                                                                          "fig2":fig2,
                                                                          "fig3":fig3,
                                                                          "fig4":fig4,
                                                                          "fig5":fig5,
                                                                          "fig6":fig6})
    


def AccessToRoadnetworkView(request):
    queryset = AccessToRoadnetwork.objects.all()

    alchemyEngine = create_engine('postgresql://postgres:PostGRE@127.0.0.1:5432/digitalpalika')
    conn = alchemyEngine.connect()
    # conn = psycopg2.connect(database='hatuwagadi', user="postgres", password="PostGRE", host="127.0.0.1", port="5432")
    query1 = "select * from access_to_roadnetwork;"
    df1 = pd.read_sql_query(query1, con=conn)
    layout = go.Layout(barmode='group')
    # config = {'displayModeBar': False}
    config = {'displaylogo': False}
    fig1 = plot(px.bar(df1, x='road_infrastructure', y='road_infrastructure_condition',
                       title='सडक सञ्जालमा पहुँच'), output_type='div', config=config, image_height=100)
    # fig1 = plot(px.pie(df1, values='road_infrastructure', names='road_infrastructure_condition',title='सडक सञ्जालमा पहुँच', height=300),output_type='div', config=config)
    # fig1 = px.pie(df1, values='road_infrastructure', names='road_infrastructure_condition',title='सडक सञ्जालमा पहुँच', height=300)
    # piechart = fig1.to_html(full_html=False, include_plotlyjs=False)
    conn.close()
    return render(request, "dprofile/accesstoroadnetwork.html", context={'queryset': queryset, "fig1": fig1})


def AgriLivstkCooperativesView(request):
    queryset = AgriLivstkCooperatives.objects.all()

    # alchemyEngine = create_engine('postgresql://postgres:PostGRE@127.0.0.1:5432/hatuwagadi')
    # conn = alchemyEngine.connect()
    # # conn = psycopg2.connect(database='hatuwagadi', user="postgres", password="PostGRE", host="127.0.0.1", port="5432")
    # query1 = "select * from agri_livstk_cooperatives;"
    # df1 = pd.read_sql_query(query1,con=conn)
    # layout = go.Layout(barmode='group')
    # # config = {'displayModeBar': False}
    # config = {'displaylogo': False}
    # fig1 = plot(px.bar(df1, x='road_infrastructure', y='road_infrastructure_condition',
    #        title='सडक सञ्जालमा पहुँच'), output_type='div', config=config, image_height=100)
    # # fig1 = plot(px.pie(df1, values='road_infrastructure', names='road_infrastructure_condition',title='सडक सञ्जालमा पहुँच', height=300),output_type='div', config=config)
    # # fig1 = px.pie(df1, values='road_infrastructure', names='road_infrastructure_condition',title='सडक सञ्जालमा पहुँच', height=300)
    # # piechart = fig1.to_html(full_html=False, include_plotlyjs=False)
    # conn.close()
    return render(request, "dprofile/agrilivstkcooperative.html", context={'queryset': queryset})


def AnimalHusbandryFirmsView(request):
    queryset = AnimalHusbandryFirms.objects.all()

    alchemyEngine = create_engine('postgresql://postgres:PostGRE@127.0.0.1:5432/digitalpalika')
    conn = alchemyEngine.connect()
    # conn = psycopg2.connect(database='hatuwagadi', user="postgres", password="PostGRE", host="127.0.0.1", port="5432")
    query1 = "select * from animal_husbandry_firms;"
    df1 = pd.read_sql_query(query1, con=conn)
    layout = go.Layout(barmode='group')
    # config = {'displayModeBar': False}
    config = {'displaylogo': False}
    fig1 = plot(px.bar(df1, x='products', y='amount_produced',
                       title='आधुनिक पशुपालन (फार्म) सम्बन्धी विवरण'), output_type='div', config=config,
                image_height=100)
    # fig1 = plot(px.pie(df1, values='road_infrastructure', names='road_infrastructure_condition',title='सडक सञ्जालमा पहुँच', height=300),output_type='div', config=config)
    # fig1 = px.pie(df1, values='road_infrastructure', names='road_infrastructure_condition',title='सडक सञ्जालमा पहुँच', height=300)
    # piechart = fig1.to_html(full_html=False, include_plotlyjs=False)
    conn.close()
    return render(request, "dprofile/animalhusbandryfirms.html", context={'queryset': queryset, "fig1": fig1})



class MapView(TemplateView):
    template_name = 'map.html'

    def get_context_data(self, **kwargs):
        figure = folium.Figure()

        # generate base data
        data = (np.random.normal(size=(100, 2)) * np.array([[1, 1]]) +
                np.array([[48, 5]]))
        
        

        # make a map
        m = folium.Map(
            location=[27.0149456, 87.1688135],
            zoom_start=11,
            tiles='OpenStreetMap',
            control_scale=True,
            height='90%',
            max_bounds=True,
            
            
        )

        url = 'dprofile/static/hh_survey_4 July_2024.json'
        gdf = geopandas.read_file("dprofile/static/hh_survey_4 July_2024.json")
        gdf.head()

        folium.GeoJson(gdf,
                       name="Household Heads",
                       zoom_on_click=True,
                       marker=folium.Marker(icon=folium.Icon(icon='star')),
                       tooltip=folium.GeoJsonTooltip(fields=["Name:", "House Number", "Ward Number"]),
                       popup=folium.GeoJsonPopup(
                           fields=["Name:", "House Number", "Tole", "Ward Number", "Phone Number"]),
                       smooth_factor=10,
                       ).add_to(m)

        m.add_to(figure)

        household = folium.GeoJson(gdf,
                                   name="Household Heads",
                                   zoom_on_click=True,
                                   marker=folium.Marker(icon=folium.Icon(icon='star')),
                                   tooltip=folium.GeoJsonTooltip(fields=["Name:", "House Number", "Ward Number"]),
                                   popup=folium.GeoJsonPopup(
                                       fields=["Name:", "House Number", "Tole", "Ward Number", "Phone Number"]),
                                   smooth_factor=10,
                                   ).add_to(m)

        m.add_to(figure)

        householdsearch = Search(
            layer=household,
            geom_type="Point",
            placeholder="Serach for a household name",
            collapsed=True,
            search_label="Name in Block Letter",
        ).add_to(m)

        # generat the data to segment by (levels of another pandas column in practical usage)
        categories = ['category{}'.format(i + 1) for i in range(30)]
        category_column = [random.choice(categories) for i in range(len(data))]

        # create map and add the data with additional parameter tags as the segmentation
        for i, latlng in enumerate(data):
            category = category_column[i]
            folium.Marker(
                tuple(latlng),
                tags=[category]
            ).add_to(m)

        TagFilterButton(categories).add_to(m)

        # fetch the objects from database and make markers for them
        # for house in HhSurvey.objects.all():
        #     make_markers_and_add_to_map(m, house)

        # render and send to template
        figure.render()
        return {"map": figure}

        folium.LayerControl().add_to(m)
