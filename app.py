import re
from hashlib import md5
from flask import Flask, render_template
app = Flask(__name__)

big_areas = (
    ("Computer Science", [
        ("data structures", [
            """Doesn't know the difference between Array and LinkedList""",
            """Able to explain and use Arrays, LinkedLists, Dictionaries etc in practical programming tasks""",
            """Knows space and time tradeoffs of the basic data structures, Arrays vs LinkedLists, Able to explain how hashtables can be implemented and can handle collisions, Priority queues and ways to implement them etc.""",
            """Knowledge of advanced data structures like B-trees, binomial and fibonacci heaps, AVL/Red Black trees, Splay Trees, Skip Lists, tries etc.""",
        ]),
        ("algorithms", [
            """Unable to find the average of numbers in an array (It's hard to believe but I've interviewed such candidates) """,
            """Basic sorting, searching and data structure traversal and retrieval algorithms """,
            """Tree, Graph, simple greedy and divide and conquer algorithms, is able to understand the relevance of the levels of this matrix. """,
            """Able to recognize and code dynamic programming solutions, good knowledge of graph algorithms, good knowledge of numerical computation algorithms, able to identify NP problems etc. """,
        ]),
        ("systems programming", [
            """Doesn't know what a compiler, linker or interpreter is""",
            """Basic understanding of compilers, linker and interpreters. Understands what assembly code is and how things work at the hardware level. Some knowledge of virtual memory and paging.""",
            """Understands kernel mode vs. user mode, multi-threading, synchronization primitives and how they're implemented, able to read assembly code. Understands how networks work, understanding of network protocols and socket level programming.""",
            """Understands the entire programming stack, hardware (CPU + Memory + Cache + Interrupts + microcode), binary code, assembly, static and dynamic linking, compilation, interpretation, JIT compilation, garbage collection, heap, stack, memory addressing...""",
        ]),
    ]),


    ("Software Engineering", [
        ("source code version control", [
            """Folder backups by date""",
            """VSS and beginning CVS/SVN user""",
            """Proficient in using CVS and SVN features. Knows how to branch and merge, use patches setup repository properties etc.""",
            """Knowledge of distributed VCS systems. Has tried out Bzr/Mercurial/Darcs/Git""",
        ]),
        ("build automation", [
            """Only knows how to build from IDE""",
            """Knows how to build the system from the command line""",
            """Can setup a script to build the basic system""",
            """Can setup a script to build the system and also documentation, installers, generate release notes and tag the code in source control""",
        ]),
        ("automated testing", [
            """Thinks that all testing is the job of the tester""",
            """Has written automated unit tests and comes up with good unit test cases for the code that is being written""",
            """Has written code in TDD manner""",
            """Understands and is able to setup automated functional, load/performance and UI tests""",
        ])
    ]),

    ("Programming", [
        ("problem decomposition", [
            """Only straight line code with copy paste for reuse""",
            """Able to break up problem into multiple functions""",
            """Able to come up with reusable functions/objects that solve the overall problem""",
            """Use of appropriate data structures and algorithms and comes up with generic/object-oriented code that encapsulate aspects of the problem that are subject to change.""",
        ]),
        ("systems decomposition", [
            """Not able to think above the level of a single file/class""",
            """Able to break up problem space and design solution as long as it is within the same platform/technology""",
            """Able to design systems that span multiple technologies/platforms.""",
            """Able to visualize and design complex systems with multiple product lines and integrations with external systems. Also should be able to design operations support systems like monitoring, reporting, fail overs etc.""",
        ]),
        ("communication", [
            """Cannot express thoughts/ideas to peers. Poor spelling and grammar.""",
            """Peers can understand what is being said. Good spelling and grammar.""",
            """Is able to effectively communicate with peers""",
            """Able to understand and communicate thoughts/design/ideas/specs in a unambiguous manner and adjusts communication as per the context""",
        ]),
        ("code organization within a file", [
            """no evidence of organization within a file""",
            """Methods are grouped logically or by accessibility""",
            """Code is grouped into regions and well commented with references to other source files""",
            """File has license header, summary, well commented, consistent white space usage. The file should look beautiful.""",
        ]),
        ("code organization across files", [
            """No thought given to organizing code across files""",
            """Related files are grouped into a folder""",
            """Each physical file has a unique purpose, for e.g. one class definition, one feature implementation etc.""",
            """Code organization at a physical level closely matches design and looking at file names and folder distribution provides insights into design""",
        ]),
        ("source tree organization", [
          """Everything in one folder""",
          """Basic separation of code into logical folders.""",
          """No circular dependencies, binaries, libs, docs, builds, third-party code all organized into appropriate folders""",
          """Physical layout of source tree matches logical hierarchy and organization.  The directory names and organization provide insights into the design of the system.""",
        ]),
        ("code readability", [
          """Mono-syllable names""",
          """Good names for files, variables classes, methods etc.""",
          """No long functions, comments explaining unusual code, bug fixes, code assumptions""",
          """Code assumptions are verified using asserts, code flows naturally - no deep nesting of conditionals or methods""",
        ]),
        ("defensive coding", [
          """Doesn't understand the concept""",
          """Checks all arguments and asserts critical assumptions in code""",
          """Makes sure to check return values and check for exceptions around code that can fail.""",
          """Has his own library to help with defensive coding, writes unit tests that simulate faults""",
        ]),
        ("error handling", [
          """Only codes the happy case""",
          """Basic error handling around code that can throw exceptions/generate errors""",
          """Ensures that error/exceptions leave program in good state, resources, connections and memory is all cleaned up properly""",
          """Codes to detect possible exception before, maintain consistent exception handling strategy in all layers of code, come up with guidelines on exception handling for entire system.""",
        ]),
        ("IDE", [
          """Mostly uses IDE for text editing""",
          """Knows their way around the interface, able to effectively use the IDE using menus.""",
          """Knows keyboard shortcuts for most used operations.""",
          """Has written custom macros""",
        ]),
        ("API", [
          """Needs to look up the documentation frequently""",
          """Has the most frequently used APIs in memory""",
          """Vast and In-depth knowledge of the API""",
          """Has written libraries that sit on top of the API to simplify frequently used tasks and to fill in gaps in the API""",
        ]),
        ("frameworks", [
          """Has not used any framework outside of the core platform""",
          """Has heard about but not used the popular frameworks available for the platform.""",
          """Has used more than one framework in a professional capacity and is well-versed with the idioms of the frameworks.""",
          """Author of framework""",
        ]),
        ("requirements", [
          """Takes the given requirements and codes to spec""",
          """Come up with questions regarding missed cases in the spec""",
          """Understand complete picture and come up with entire areas that need to be speced""",
          """Able to suggest better alternatives and flows to given requirements based on experience""",
        ]),
        ("scripting", [
          """No knowledge of scripting tools""",
          """Batch files/shell scripts""",
          """Perl/Python/Ruby/VBScript/Powershell""",
          """Has written and published reusable code""",
        ]),
        ("database", [
          """Thinks that Excel is a database""",
          """Knows basic database concepts, normalization, ACID, transactions and can write simple selects""",
          """Able to design good and normalized database schemas keeping in mind the queries that'll have to be run, proficient in use of views, stored procedures, triggers and user defined types. Knows difference between clustered and non-clustered indexes. Proficient in use of ORM tools.""",
          """Can do basic database administration, performance optimization, index optimization, write advanced select queries, able to replace cursor usage with relational sql, understands how data is stored internally, understands how indexes are stored internally, understands how databases can be mirrored, replicated etc. Understands how the two phase commit works.""",
        ]),

    ]),

    ("Knowledge", [
        ("tool knowledge", [
            """Limited to primary IDE (VS.Net, Eclipse etc.)""",
            """Knows about some alternatives to popular and standard tools.""",
            """Good knowledge of editors, debuggers, IDEs, open source alternatives etc.  etc. For e.g. someone who knows most of the tools from Scott Hanselman's power tools list. Has used ORM tools.""",
            """Has actually written tools and scripts, added bonus if they've been published.""",
        ]),
        ("languages exposed to", [
            """Imperative or Object Oriented""",
            """Imperative, Object-Oriented and declarative (SQL), added bonus if they understand static vs dynamic typing, weak vs strong typing and static inferred types""",
            """Functional, added bonus if they understand lazy evaluation, currying, continuations""",
            """Concurrent (Erlang, Oz) and Logic (Prolog)""",
        ]),
        ("codebase knowledge", [
            """Has never looked at the codebase""",
            """Basic knowledge of the code layout and how to build the system""",
            """Good working knowledge of code base, has implemented several bug fixes and maybe some small features.""",
            """Has implemented multiple big features in the codebase and can easily visualize the changes required for most features or bug fixes.""",
        ]),
        ("knowledge of upcoming technologies", [
            """Has not heard of the upcoming technologies""",
            """Has heard of upcoming technologies in the field""",
            """Has downloaded the alpha preview/CTP/beta and read some articles/manuals""",
            """Has played with the previews and has actually built something with it and as a bonus shared that with everyone else""",
        ]),
        ("platform internals", [
            """Zero knowledge of platform internals""",
            """Has basic knowledge of how the platform works internally""",
            """Deep knowledge of platform internals and can visualize how the platform takes the program and converts it into executable code.""",
            """Has written tools to enhance or provide information on platform internals.  For e.g. disassemblers, decompilers, debuggers etc.""",
        ]),
        ("books", [
            """Unleashed series, 21 days series, 24 hour series, dummies series...""",
            """Code Complete, Don't Make me Think, Mastering Regular Expressions""",
            """Design Patterns, Peopleware, Programming Pearls, Algorithm Design Manual, Pragmatic Programmer, Mythical Man month""",
            """Structure and Interpretation of Computer Programs, Concepts Techniques, Models of Computer Programming, Art of Computer Programming, Database systems , by C. J Date, Thinking Forth, Little Schemer""",
        ]),
        ("blogs", [
            """Has heard of them but never got the time.""",
            """Reads tech/programming/software engineering blogs and listens to podcasts regularly.""",
            """Maintains a link blog with some collection of useful articles and tools that he/she has collected""",
            """Maintains a blog in which personal insights and thoughts on programming are shared""",
        ]),
    ]),

    ("Experience", [
        ("languages with professional experience", [
            """Imperative or Object Oriented""",
            """Imperative, Object-Oriented and declarative (SQL), added bonus if they understand static vs dynamic typing, weak vs strong typing and static inferred types""",
            """Functional, added bonus if they understand lazy evaluation, currying, continuations""",
            """Concurrent (Erlang, Oz) and Logic (Prolog)""",
        ]),

        ("platforms with professional experience", [
            """1""",
            """2-3""",
            """4-5""",
            """6+""",
        ]),

        ("years of professional experience", [
            """1""",
            """2-5""",
            """6-9""",
            """10+""",
        ]),

        ("domain knowledge", [
            """No knowledge of the domain""",
            """Has worked on at least one product in the domain.""",
            """Has worked on multiple products in the same domain.""",
            """Domain expert. Has designed and implemented several products/solutions in the domain. Well versed with standard terms, protocols used in the domain.""",
        ]),
    ]),
)


skills = "languages_with_professional_experienceimperative_or_object_oriented=on&languages_with_professional_experienceimperative__object_oriented_and_declarative__sql___added_bonus_if_they_understand_static_vs_dynamic_typing__weak_vs_strong_typing_and_static_inferred_types=on&languages_with_professional_experiencefunctional__added_bonus_if_they_understand_lazy_evaluation__currying__continuations=on&platforms_with_professional_experience6_=on&years_of_professional_experience10_=on&domain_knowledgehas_worked_on_multiple_products_in_the_same_domain_=on&problem_decompositionable_to_break_up_problem_into_multiple_functions=on&problem_decompositionable_to_come_up_with_reusable_functions_objects_that_solve_the_overall_problem=on&problem_decompositionuse_of_appropriate_data_structures_and_algorithms_and_comes_up_with_generic_object_oriented_code_that_encapsulate_aspects_of_the_problem_that_are_subject_to_change_=on&systems_decompositionable_to_break_up_problem_space_and_design_solution_as_long_as_it_is_within_the_same_platform_technology=on&systems_decompositionable_to_design_systems_that_span_multiple_technologies_platforms_=on&systems_decompositionable_to_visualize_and_design_complex_systems_with_multiple_product_lines_and_integrations_with_external_systems__also_should_be_able_to_design_operations_support_systems_like_monitoring__reporting__fail_overs_etc_=on&communicationpeers_can_understand_what_is_being_said__good_spelling_and_grammar_=on&communicationis_able_to_effectively_communicate_with_peers=on&communicationable_to_understand_and_communicate_thoughts_design_ideas_specs_in_a_unambiguous_manner_and_adjusts_communication_as_per_the_context=on&code_organization_within_a_filemethods_are_grouped_logically_or_by_accessibility=on&code_organization_within_a_filecode_is_grouped_into_regions_and_well_commented_with_references_to_other_source_files=on&code_organization_within_a_filefile_has_license_header__summary__well_commented__consistent_white_space_usage__the_file_should_look_beautiful_=on&code_organization_across_filesrelated_files_are_grouped_into_a_folder=on&code_organization_across_fileseach_physical_file_has_a_unique_purpose__for_e_g__one_class_definition__one_feature_implementation_etc_=on&code_organization_across_filescode_organization_at_a_physical_level_closely_matches_design_and_looking_at_file_names_and_folder_distribution_provides_insights_into_design=on&source_tree_organizationbasic_separation_of_code_into_logical_folders_=on&source_tree_organizationno_circular_dependencies__binaries__libs__docs__builds__third_party_code_all_organized_into_appropriate_folders=on&source_tree_organizationphysical_layout_of_source_tree_matches_logical_hierarchy_and_organization___the_directory_names_and_organization_provide_insights_into_the_design_of_the_system_=on&code_readabilityno_long_functions__comments_explaining_unusual_code__bug_fixes__code_assumptions=on&code_readabilitycode_assumptions_are_verified_using_asserts__code_flows_naturally___no_deep_nesting_of_conditionals_or_methods=on&defensive_codingchecks_all_arguments_and_asserts_critical_assumptions_in_code=on&defensive_codingmakes_sure_to_check_return_values_and_check_for_exceptions_around_code_that_can_fail_=on&error_handlingbasic_error_handling_around_code_that_can_throw_exceptions_generate_errors=on&error_handlingensures_that_error_exceptions_leave_program_in_good_state__resources__connections_and_memory_is_all_cleaned_up_properly=on&error_handlingcodes_to_detect_possible_exception_before__maintain_consistent_exception_handling_strategy_in_all_layers_of_code__come_up_with_guidelines_on_exception_handling_for_entire_system_=on&ideknows_their_way_around_the_interface__able_to_effectively_use_the_ide_using_menus_=on&ideknows_keyboard_shortcuts_for_most_used_operations_=on&idehas_written_custom_macros=on&apihas_the_most_frequently_used_apis_in_memory=on&apivast_and_in_depth_knowledge_of_the_api=on&apihas_written_libraries_that_sit_on_top_of_the_api_to_simplify_frequently_used_tasks_and_to_fill_in_gaps_in_the_api=on&frameworkshas_heard_about_but_not_used_the_popular_frameworks_available_for_the_platform_=on&frameworkshas_used_more_than_one_framework_in_a_professional_capacity_and_is_well_versed_with_the_idioms_of_the_frameworks_=on&requirementscome_up_with_questions_regarding_missed_cases_in_the_spec=on&requirementsunderstand_complete_picture_and_come_up_with_entire_areas_that_need_to_be_speced=on&requirementsable_to_suggest_better_alternatives_and_flows_to_given_requirements_based_on_experience=on&scriptingbatch_files_shell_scripts=on&scriptingperl_python_ruby_vbscript_powershell=on&databaseknows_basic_database_concepts__normalization__acid__transactions_and_can_write_simple_selects=on&databaseable_to_design_good_and_normalized_database_schemas_keeping_in_mind_the_queries_that_ll_have_to_be_run__proficient_in_use_of_views__stored_procedures__triggers_and_user_defined_types__knows_difference_between_clustered_and_non_clustered_indexes__proficient_in_use_of_orm_tools_=on&databasecan_do_basic_database_administration__performance_optimization__index_optimization__write_advanced_select_queries__able_to_replace_cursor_usage_with_relational_sql__understands_how_data_is_stored_internally__understands_how_indexes_are_stored_internally__understands_how_databases_can_be_mirrored__replicated_etc__understands_how_the_two_phase_commit_works_=on&source_code_version_controlvss_and_beginning_cvs_svn_user=on&source_code_version_controlproficient_in_using_cvs_and_svn_features__knows_how_to_branch_and_merge__use_patches_setup_repository_properties_etc_=on&source_code_version_controlknowledge_of_distributed_vcs_systems__has_tried_out_bzr_mercurial_darcs_git=on&build_automationknows_how_to_build_the_system_from_the_command_line=on&build_automationcan_setup_a_script_to_build_the_basic_system=on&build_automationcan_setup_a_script_to_build_the_system_and_also_documentation__installers__generate_release_notes_and_tag_the_code_in_source_control=on&automated_testinghas_written_automated_unit_tests_and_comes_up_with_good_unit_test_cases_for_the_code_that_is_being_written=on&automated_testinghas_written_code_in_tdd_manner=on&automated_testingunderstands_and_is_able_to_setup_automated_functional__load_performance_and_ui_tests=on&data_structuresable_to_explain_and_use_arrays__linkedlists__dictionaries_etc_in_practical_programming_tasks=on&data_structuresknows_space_and_time_tradeoffs_of_the_basic_data_structures__arrays_vs_linkedlists__able_to_explain_how_hashtables_can_be_implemented_and_can_handle_collisions__priority_queues_and_ways_to_implement_them_etc_=on&data_structuresknowledge_of_advanced_data_structures_like_b_trees__binomial_and_fibonacci_heaps__avl_red_black_trees__splay_trees__skip_lists__tries_etc_=on&algorithmsbasic_sorting__searching_and_data_structure_traversal_and_retrieval_algorithms_=on&algorithmstree__graph__simple_greedy_and_divide_and_conquer_algorithms__is_able_to_understand_the_relevance_of_the_levels_of_this_matrix__=on&algorithmsable_to_recognize_and_code_dynamic_programming_solutions__good_knowledge_of_graph_algorithms__good_knowledge_of_numerical_computation_algorithms__able_to_identify_np_problems_etc__=on&systems_programmingbasic_understanding_of_compilers__linker_and_interpreters__understands_what_assembly_code_is_and_how_things_work_at_the_hardware_level__some_knowledge_of_virtual_memory_and_paging_=on&systems_programmingunderstands_kernel_mode_vs__user_mode__multi_threading__synchronization_primitives_and_how_they_re_implemented__able_to_read_assembly_code__understands_how_networks_work__understanding_of_network_protocols_and_socket_level_programming_=on&systems_programmingunderstands_the_entire_programming_stack__hardware__cpu___memory___cache___interrupts___microcode___binary_code__assembly__static_and_dynamic_linking__compilation__interpretation__jit_compilation__garbage_collection__heap__stack__memory_addressing___"


def skill_hash_function(skill):
    return md5(skill).hexdigest()

def slugify(text):
    return re.sub(r"\W", "_", text.lower())

def reverse(coll):
    return list(reversed(coll))
l = []
for x in skills.split('&'): l.append(x[:-3])

app.jinja_env.globals.update(reverse=reverse,enumerate=enumerate,len=len,slugify=slugify,big_areas=big_areas,user_skills=l)
@app.route("/")
def index():
    return render_template('index.html') 


@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

values = {
	"enumerate": enumerate,
	"reverse": reverse,
	"len": len,
	"slugify": slugify,
	"big_areas": big_areas,
#	"logout_url": users.create_logout_url("/"),
#	"login_url": users.create_login_url(self.request.uri),
    }
if __name__ == "__main__":
    app.run(debug=True)
